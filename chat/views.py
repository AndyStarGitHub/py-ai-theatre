from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .ai_agent import call_ai_agent


@login_required
def chat_view(request: HttpRequest) -> HttpResponse:
    user = request.user

    if request.method == 'POST':
        content = request.POST.get('message', '').strip()
        if content:
            Message.objects.create(
                user=user,
                role='user',
                content=content
            )

            history = (Message.
                       objects.filter(user=user).
                       order_by('created_at')
                       )
            messages_for_ai = [
                {"role": m.role, "content": m.content}
                for m in history
            ]

            ai_reply = call_ai_agent(messages_for_ai, user.id)

            Message.objects.create(
                user=user,
                role='assistant',
                content=ai_reply
            )

        return redirect('chat')

    messages = Message.objects.filter(user=user).order_by('created_at')

    return render(request, 'chat/chat.html', {'messages': messages})


@login_required
def clear_history_view(request: HttpRequest) -> HttpResponse:
    Message.objects.filter(user=request.user).delete()
    messages.success(request, "Chat history cleared.")
    return redirect('chat')
