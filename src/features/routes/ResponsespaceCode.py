from features.routes.NamespaceCode import NamespaceCode, fields

class ResponsespaceCode(NamespaceCode):
    def __init__(self, name, description=None, path=None):
        self.body = {
        }
        super().__init__(name, description, path)
    
    def buildBody(self, code, message, data, status):
        self.body = {
            'code': fields.Integer(code),
            'message': fields.String(message),
            'data': data,
            'status': fields.String(status)
        }

    def responseCompiler(self):
        return fields.Nested(self.model('data', {
            'memory_used': fields.Float(0.0, description='Memory used in bytes'),
            'result': fields.String('', description='Result of the execution'),
            'time_execution': fields.Float(0.0, description='Time of execution in seconds'),
        }))

    def responseAssertCompile(self):
        self.buildBody(
                200, 
                'Great job! Your code compiled successfully! 🎉🚀',
                self.responseCompiler(),
                'OK')
        return self.model('response_assert_compile', self.body)

    def responseErrorCompile(self):
        self.buildBody(
                400,
                'Compilation failed. Don\'t give up! Check your code and try again. 💡🔧',
                self.responseCompiler(),
                'Error')
        return self.model('response_error_compile', self.body)

    def responseAssert(self):
        return fields.List(fields.Nested(self.model('data', {
                'memory_used': fields.Float(0.0, description='Memory used in bytes'),
                'result': fields.String('', description='Result of the execution'),
                'time_execution': fields.Float(0.0, description='Time of execution in seconds'),
            })), min_items=1, max_items=5)
    
    def responseAssertAssert(self):
        self.buildBody(
            200,
            'Evaluation completed! Here are your results. 🌟📊',
            self.responseAssert(),
            'OK'
        )
        return self.model('response_assert_assert', self.body)
    
    def responseErrorAssert(self):
        self.buildBody(
            400,
            'Review list of compilation for your code. 💡🔧',
            self.responseAssert(),
            'Error'
        )
        return self.model('response_error_assert', self.body)