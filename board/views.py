from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.db.models import Model
from .models import Document, Comment
from .forms import DocumentForm

# Create your views here.


def index(request):
    if request.method == 'GET':
        document_list = Document.objects.order_by('-Did')
        context = {'document_list': document_list}
        return render(request, 'board/document_list.html', context)


def write(request):
    if request.method == 'GET':
        form = DocumentForm()
        return render(request, 'board/write_form.html', {'form': form})

    elif request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            doc = Document(
                title=form.cleaned_data.get('title'),
                content=form.cleaned_data.get('content'),
                author=request.user
            )
            doc.save()
            return redirect('board:index')


def read(request, Did):
    if request.method != 'GET':
        return HttpResponseBadRequest('Invalid Method')

    doc = Document.objects.get(Did=Did)
    comments = Comment.objects.order_by('-created_at').filter(Doc__Did=Did)
    if comments:
        for c in comments:
            if c.author.username == request.user.username:
                c.ownership = True
    if doc:
        content = {
            'Did': doc.Did,
            'title': doc.title,
            'content': doc.content,
            'author': doc.author.username,
            'ownership': False
        }
        if doc.author.username == request.user.username:
            content['ownership'] = True
        return render(request, 'board/read.html', {'doc': content, 'comments': comments})


def delete(request, Did):
    if request.method != 'GET' or type(Did) is not int:
        return HttpResponseBadRequest('Invalid method or parameter')

    doc = Document.objects.get(Did=Did)
    if not doc:
        return HttpResponseBadRequest(f'Can not find Document with id {Did}')

    if doc.author.username == request.user.username:
        doc.delete()
        return redirect('board:index')


def edit(request, Did):
    doc = Document.objects.get(Did=Did)

    if request.method == 'GET':
        form = {
            'title': doc.title,
            'content': doc.content
        }
        form = DocumentForm(form)
        print(form)
        return render(request, 'board/write_form.html', {'form': form})

    elif request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid() and doc.author.username == request.user.username:
            doc.title = form.cleaned_data.get('title')
            doc.content = form.cleaned_data.get('content')
            doc.save()
            return redirect('board:index')

        else:
            return HttpResponseBadRequest("Invalid Value or Don't Have Permission")


def comment(request, Did):
    if request.method == 'POST':
        comm = Comment(
            Doc=Document.objects.get(Did=Did),
            author=request.user,
            content=request.POST['comment']
        )
        comm.save()
        return redirect("board:read", Did=Did)


def comment_delete(request, Cid):
    if request.method != 'GET':
        return HttpResponseBadRequest("Invalid Method")

    comm = Comment.objects.get(Cid=Cid)
    if comm.author.username == request.user.username:
        comm.delete()
        return redirect('board:index')

    else:
        return HttpResponseBadRequest('No Permission')
