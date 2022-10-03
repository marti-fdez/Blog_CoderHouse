from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from Messages.forms import MessageForm
from Messages.models import Chat, Message

class NewChatView(LoginRequiredMixin, CreateView):
    model = Chat 
    fields= ['user2']
    success_url = reverse_lazy('chats')
    template_name= "newchat.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user1 = self.request.user
        self.object.save()        
        return HttpResponseRedirect(self.get_success_url())

class ChatList(LoginRequiredMixin, ListView):
    model = Chat 
    template_name= "chats.html"

@login_required  # type: ignore
def detalle_chat(request, pk):
    chat_identifier = Chat.objects.get(id=pk)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            mensaje = Message(text=data['text'], chat_id=chat_identifier, author=request.user)
            mensaje.save()
            return redirect(reverse('detalle-chat', kwargs={'pk':pk}))
    else:
        form = MessageForm()
        return render(request, 'detalle-chat.html', {"form": form, 'object': chat_identifier})

class EliminarChat(LoginRequiredMixin, DeleteView):
    model = Chat
    success_url = reverse_lazy('chats')
    template_name= "eliminar.html"

@login_required  # type: ignore
def new_message_view(request, pk):
    chat_identifier = Chat.objects.get(id=pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            mensaje = Message(text=data['text'], chat_id=chat_identifier, author=request.user)
            mensaje.save()
            return redirect(reverse('detalle-chat', kwargs={'pk':pk}))
    else:
        form = MessageForm()
        return render(request, 'newmessage.html', {"form": form})