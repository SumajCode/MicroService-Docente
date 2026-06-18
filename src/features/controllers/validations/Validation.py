from flask_wtf import FlaskForm

from scripts.FormaterString import formatErrorsValidate

class ValidationForm(FlaskForm):
    def validate(self):
        form = ValidationForm(meta={'csrf':False})
        if not form.validate_on_submit():
            return self.response({
                'data':[],
                'message': formatErrorsValidate(form.errors),
                'status': 'Error',
                'code': 200
            })