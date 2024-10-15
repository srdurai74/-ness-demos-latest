def before_all(context):
    print('Before all')

def after_all(context):
    print('after all')

def before_tag(context,tag):
    print('before tags')

def after_tag(context,tag):
    print('after tags')

def before_feature(context,feature):
    print('before feature')

def after_feature(context,feature):
    print('after feature')

def before_scenario(context,scenario):
    print('before scenario')

def after_scenario(context,scenario):
    print('after scenario')

def before_step(context,step):
    print('before step')

def after_step(context,step):
    print('after step')
