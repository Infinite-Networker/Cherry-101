class Frame:
    def __init__(self, rows): self.rows = rows
    def describe(self): return {'rows': len(self.rows)}
class Model:
    def __init__(self, name, leaderboard): self.name=name; self.leaderboard=leaderboard
    def predict_mock(self, rows):
        out=[]
        for r in rows:
            out.append({'prediction':1 if r.get('amount',0)>80 else 0, 'actual': r.get('is_return')})
        return out
class Endpoint:
    def __init__(self, url): self.url=url
class Database:
    def __init__(self, uri, user=None, password=None): self.uri=uri
    def query(self, sql, params=None):
        if 'orders_test' in sql.lower():
            return [{'id':1,'status':'shipped','is_return':0,'amount':110.0},{'id':2,'status':'shipped','is_return':1,'amount':40.0}]
        return [{'id':1,'status':'shipped','is_return':0,'amount':100.0},{'id':2,'status':'shipped','is_return':1,'amount':50.0}]
def to_frame(val): return Frame(val if isinstance(val,list) else [])
def automl_train(frame, target, max_runtime_secs=60): return Model('mock', [{'model':'m','auc':0.9}])
def deploy_model(model, endpoint_url='http://127.0.0.1:8080/predict'): return Endpoint(endpoint_url)
def undeploy_controller(ctrl, timeout=5.0): return True
def evaluate_predictions(preds, label_col='is_return'):
    rows = preds if isinstance(preds,list) else preds
    TP=FP=TN=FN=0
    for r in rows:
        p = r.get('prediction'); a = r.get('actual') if 'actual' in r else r.get(label_col)
        if a is None: continue
        p=int(p); a=int(a)
        if p==1 and a==1: TP+=1
        if p==1 and a==0: FP+=1
        if p==0 and a==0: TN+=1
        if p==0 and a==1: FN+=1
    total=TP+FP+TN+FN
    acc=(TP+TN)/total if total>0 else 0.0
    prec=TP/(TP+FP) if (TP+FP)>0 else 0.0
    rec=TP/(TP+FN) if (TP+FN)>0 else 0.0
    f1=(2*prec*rec)/(prec+rec) if (prec+rec)>0 else 0.0
    return {'accuracy':acc,'precision':prec,'recall':rec,'f1':f1,'confusion_matrix':{'TP':TP,'FP':FP,'TN':TN,'FN':FN}}
def write_json_report(report, path='evaluation.json'):
    import json
    with open(path,'w') as f: json.dump(report,f,indent=2)
    return path
