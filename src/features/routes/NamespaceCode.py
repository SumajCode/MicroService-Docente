from flask_restx import Namespace, Resource, fields

class NamespaceCode(Namespace):
    def __init__(self, name, description=None, path=None):
        self.resource = Resource
        self.fieldsCode = None
        super().__init__(name, description, path)
    
    def fieldsCompiler(self):
        self.fieldsCode = {
            'code': fields.String(),
            'lang': fields.String(),
        }
        return self.model('code', self.fieldsCode)

    def fieldsAssert(self):
        self.fieldsCompiler()
        self.fieldsCode['inputs'] = fields.List(fields.Raw)
        self.fieldsCode['outputs'] = fields.List(fields.Raw)
        self.fieldsCode['invokFunction'] = fields.String()

        modelFunctions = self.model('functions', {
                'functionNames': fields.List(fields.String('func')),
                'functionCode': fields.List(fields.String('def func(): \nreturn None'))
            })
        modelClass = self.model('class', {
            'classNames': fields.List(fields.String('clas')),
            'classCode': fields.List(fields.String('class clas(): \ndef __init__(self):\nreturn None'))
            })

        self.fieldsCode['rules'] = fields.Nested(self.model('rules', {
            'functions': fields.Nested(modelFunctions),
            'classes': fields.Nested(modelClass)
        }))
        return self.model('asset', self.fieldsCode)