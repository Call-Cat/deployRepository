from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib import messages
from .models import Memos
from django.http import Http404


# Create your views here.
def create_memo(request):
    create_memo_form = forms.CreateMemoForm(request.POST or None)
    if create_memo_form.is_valid():
        create_memo_form.instance.user = request.user
        messages.success(request, 'メモを作成しました。')
        return redirect('boards:list_memos')
    return render(
        request, 'boards/create_memo.html', context={
            'create_memo_form': create_memo_form,
        }
    )


def list_memos(request):
    memos = Memos.objects
    return render(
        request, 'boards/list_memos.html', context={
            'memos': memos
        }
    )


def edit_memo(request, id):
    memo = get_object_or_404(Memos, id=id)
    if memo.user.id != request.user.id:
        raise Http404
    edit_memo_form = forms.CreateMemoForm(request.POST or None, instance=memo)
    if edit_memo_form.is_valid():
        edit_memo_form.save()
        messages.success(request, 'メモを更新しました')
        return redirect('boards:list_memos')
    return render(
        request, 'boards/edit_memo.html', context={
            'edit_memo_form': edit_memo_form,
            'id': id,
        }
    )


def delete_memo(request, id):
    memo = get_object_or_404(Memos, id=id)
    if memo.user.id != request.user.id:
        raise Http404
    delete_memo_form = forms.DeleteMemoForm(request.POST or None)
    if delete_memo_form.is_valid(): # csrf check
        memo.delete()
        messages.success(request, 'メモを削除しました')
        return redirect('boards:list_memos')
    return render(
        request, 'boards/delete_memo.html', context={
            'delete_memo_form': delete_memo_form,
        }
    )
