from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo


class UserCreateForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired('이름을 작성해주십시오.'), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 5자이상 적어주세요.'), Length(min=5),
                                                  EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])


class UserLoginForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired('이름을 작성해주십시오.'), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 5자이상 적어주세요.'), Length(min=5)])


class AddWorshipForm(FlaskForm):
    date = DateField('예배 날짜', format='%Y-%m-%d')
    part = StringField('예배 파트', validators=[DataRequired('예배 파트를 작성해주십시오. (예시. "5부")')])
    limit = IntegerField('참석자 Limit', validators=[DataRequired('최대 예배 참석자 수를 적어주십시오.')])


class RegisterSeatForm(FlaskForm):
    # seat = StringField('좌석', validators=[DataRequired('좌석을 선택해주십시오.')])
    name = StringField('이름', validators=[DataRequired('이름을 적어주십시오.')])


class ConnectForm(FlaskForm):
    code = PasswordField('접속코드', validators=[DataRequired('접속코드4자리를 적어주세요.')])

