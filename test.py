# import random

# list = ['to swim', 'very', 'to want', 'to go', 'this afternoon', 'dog', 'also', 'hot', 'today', 'I, me', 'cold', 'day', 'now', 'you', 'we, us', '(possesive)', 'morning', 'evening',
#         'to live', 'United states', 'one (unit)', 'next week', 'to have', 'instant ramen/noodles', 'to bring', 'many', 'friend',
#         ]

# x = random.choice(list)
# print(x)

# import customtkinter

# class YourApp(customtkinter.CTk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.answer_entry = customtkinter.CTkEntry(self,
#                                                    placeholder_text="Answer",
#                                                    width=160, height=40,
#                                                    font=("Arial", 20)
#                                                    )
#         self.answer_entry.place(relx=0.5, rely=0.4, anchor="center")

#         # Set focus on the entry widget
#         self.answer_entry.focus_set()

#         self.submit_button = customtkinter.CTkButton(self, 
#                                                     text="→", 
#                                                     width=20, height=40, font=("Arial Bold", 20),
#                                                     command=self.submit_answer
#                                                     )
#         self.submit_button.place(relx=0.7, rely=0.4, anchor="center")

#         # Bind the Enter key to the submit_answer method
#         self.bind('<Return>', self.on_enter_key)

#         self.after(100, self.set_focus)

#     def set_focus(self):
#         self.answer_entry.focus_set()

#     def submit_answer(self):
#         print("Button Pressed")

#     def on_enter_key(self, event):
#         self.submit_button.invoke()

# if __name__ == "__main__":
#     app = YourApp()
#     app.mainloop()

print(("W-A S Das").lower().replace(" ", ""))