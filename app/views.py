from django.shortcuts import render, redirect
from .models import Memo
from django.shortcuts import get_object_or_404
from . forms import MemoForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    memos = Memo.objects.all().order_by('-updated_datetime')
    return render(request, 'app/index.html', {'memos': memos})

def detail(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    return render(request, 'app/detail.html', {'memo': memo})


def new_memo(request):
    # POSTメソッドの場合は保存処理が行われる
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            # 保存後はindexページにリダイレクト
            return redirect('app:index')
    else:
        form = MemoForm()
    return render(request, 'app/new_memo.html', {'form': form})


# Postメソッドの時だけ削除機能を実行する
@require_POST
def delete_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect('app:index')
    
    
def edit_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        # すでに保存されている内容をフォームに表示するため、MemoFormにインスタンスを渡す
        form = MemoForm(instance=memo)
    return render(request, 'app/edit_memo.html', {'form': form, 'memo':memo })