from django.forms import ModelForm
from .models import Memo

class MemoForm(ModelForm):
    class Meta:
        # Memoモデルに対応したフォームを作成
        model = Memo
        # フォームに表示するフィールドを指定
        fields = ['title', 'text']