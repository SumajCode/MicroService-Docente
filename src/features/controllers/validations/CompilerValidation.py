from flask_wtf import FlaskForm
# from features.controllers.validations.Validation import ValidationForm
from wtforms import StringField
from wtforms.validators import ValidationError

class CodeForm(FlaskForm):
    def validateCode(self, field):
        """
        Validates the code input.

        The code input is required to compile a program. This method
        checks if the input is empty or contains only whitespace characters.
        If either condition is true, a ValidationError is raised with an
        appropriate error message.

        Parameters
        ----------
        field : str
            The code input to validate.

        Raises
        ------
        ValidationError
            If the code input is empty or contains only whitespace characters.
        """
        if not field.data or field.data.strip() == '':
            raise ValidationError('Code is with space, this input is required.')

    def validateLang(self, field):
        """
        Validates the language input.

        The language input is required to specify the programming language
        for compilation. This method checks if the input is empty or contains
        only whitespace characters. It also verifies whether the input
        language is permitted by the compiler. If any of these conditions are
        not met, a ValidationError is raised with an appropriate error message.

        Parameters
        ----------
        field : str
            The language input to validate.

        Raises
        ------
        ValidationError
            If the language input is empty or not permitted by the compiler.
        """

        if not field.data or field.data.strip() == '':
            raise ValidationError('Lang is with space, this input is required.')
        langPermited = ['python', 'c++', 'c#', 'java']
        # , 'rust', 'javascript', 'php', 'bash', 'go', 'kotlin', 'typescript', 'swift'
        if field.data not in langPermited:
            raise ValidationError('Language not permited in this compilator.')

    code = StringField('code', validators=[validateCode])
    lang = StringField('lang', validators=[validateLang])
