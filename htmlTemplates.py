# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:00:28 2023

@author: Quation
"""

css = '''
<style>
    body {
        background-color: #f4f4f4; /* Light gray for day mode */
        color: #333; /* Dark text for day mode */
    }

    .chat-container {
        display: flex;
        flex-direction: column;
        max-width: 800px;
        margin: auto;
        background-color: #fff; /* White background for day mode */
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
        border-radius: 10px; /* Rounded corners */
    }

    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: flex-start;
        transition: background-color 0.3s; /* Smooth transition for background color */
    }

    .chat-message.user {
        background-color: #5fba7d; /* Green for day mode */
        align-self: flex-end;
    }

    .chat-message.bot {
        background-color: #2b313e; /* Dark blue for day mode */
    }

    .chat-message .avatar {
        width: 20%;
        margin-right: 1rem;
    }

    .chat-message .avatar img {
        max-width: 78px;
        max-height: 78px;
        border-radius: 50%;
        object-fit: cover;
    }

    .chat-message .message {
        width: 80%;
        padding: 1rem;
        color: #fff; /* White text for day mode */
    }

    .pdf-message {
        background-color: #3498db; /* Blue for day mode */
    }

    .pdf-message .message {
        font-weight: bold;
    }

    /* Night mode styles */
    body.night-mode {
        background-color: #2c3e50; /* Dark blue-gray background for night mode */
        color: #ecf0f1; /* Light text for night mode */
    }

    .chat-container.night-mode {
        background-color: #34495e; /* Dark blue for night mode */
        box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1); /* Subtle shadow for depth */
    }

    .chat-message.user.night-mode {
        background-color: #27ae60; /* Dark green for night mode */
    }

    .chat-message.bot.night-mode {
        background-color: #34495e; /* Dark blue for night mode */
    }

    .pdf-message.night-mode {
        background-color: #2980b9; /* Dark blue for night mode */
    }
</style>

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

pdf_template = '''
<div class="chat-message pdf-message">
    <div class="avatar">
        <img src="https://your-pdf-icon-url.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
