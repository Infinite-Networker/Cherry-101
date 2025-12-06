from cherryscript.parser import split_statements, parse_call
from cherryscript.runtime.adapters import Database, to_frame, automl_train, deploy_model, evaluate_predictions, write_json_report
def eval_literal(t):
    t=t.strip()
    if t.startswith('"') and t.endswith('"'): return t[1:-1]
    if t.isdigit(): return int(t)
    return t
class Runtime:
    def __init__(self): self.env={}
    def run_call(self,name,args):
        if name=='connect':
            uri=eval_literal(args[0]); user=eval_literal(args[1]) if len(args)>1 else None; pwd=eval_literal(args[2]) if len(args)>2 else None
            return Database(uri,user,pwd)
        if name.endswith('.query'):
            var=name.split('.')[0]; db=self.env.get(var); sql=eval_literal(args[0]); return db.query(sql)
        if name=='h2o.frame':
            a=args[0]; return to_frame(self.env.get(a) if a in self.env else [])
        if name=='h2o.automl': return automl_train(None, None)
        if name=='deploy': m=args[0]; return deploy_model(self.env.get(m) if isinstance(m,str) else m, eval_literal(args[1]) if len(args)>1 else 'http://127.0.0.1:8080/predict')
        if name=='predict':
            m=args[0]; f=args[1]
            model=self.env.get(m) if isinstance(m,str) else m
            frame=self.env.get(f) if isinstance(f,str) else f
            if hasattr(model,'predict_mock'): return model.predict_mock(frame.rows if hasattr(frame,'rows') else frame)
            return []
        if name=='evaluate':
            preds=args[0]; label=eval_literal(args[1]) if len(args)>1 else 'is_return'; outfile=eval_literal(args[2]) if len(args)>2 else 'evaluation.json'
            preds_val=self.env.get(preds) if isinstance(preds,str) and preds in self.env else preds
            report = evaluate_predictions(preds_val)
            write_json_report(report, outfile)
            print('[metrics]', report)
            return report
        if name=='print':
            v=eval_literal(args[0]) if args else ''; print(v); return None
        return None
    def run_stmt(self, s):
        s=s.strip()
        if s.startswith('var '):
            name=s.split()[1]; expr='='.join(s.split('=')[1:]).strip()
            if '(' in expr and expr.endswith(')'):
                nm, args = parse_call(expr)
                res = self.run_call(nm, args)
                self.env[name]=res
                print('[env]', name, '=', res)
                return
            self.env[name]=eval_literal(expr); print('[env]', name, '=', self.env[name]); return
        if '(' in s and s.endswith(')'):
            nm,args = parse_call(s); self.run_call(nm,args); return
    def run(self, text):
        for st in split_statements(text):
            if st.strip(): self.run_stmt(st)
