import streamlit as st
from signup import signup
from login import login
from query import run_query_app
from streamlit_option_menu import option_menu

# this the fucntion to show the greater value


def myFUnc():
    print('moazzam riaz')
    i = 1
    if i == 0:
        print('the number is geater than the value')

    else:
        print('the number is not grate')

# this the recursion function to calculate the factorial


def thiFunc(n):

    input('enter to calculate factorial', n)
    if n == 0 or n == 1:
        return 1

    else:
        return n * thiFunc(n - 1)

# this the function to including inheritaNCE and method overloading polymorphism


class Animal:

    def sound():
        print('aniaml sound')


class Dog(Animal):

    def sound():
        print('boww  bpoww')


# this class is with a constructor which will be called automaticlly when the object is created
class Cat(Animal):

    def sound():
        print('meoww meoww')

    def __init__(self, a, b):

        self.a = a,
        self.b = b,


'''
the concecpts of oop
    inheritance--this concept is about the classes like we have class animanls now it will have sub classes like cat or dog this is inheritance(single level, multi level, hybrid)
    polymorphism--two methods one is method overloading which means that the function name and parameters are similar other one is method overloading in which the function name is similar but parameters are different
    encapsulation--the hiddin of data which can not be accessed from outside the class three types private, public and protected
    classes--the blueprint containing all the infomartion of the particular rela world thing contain functuion or methods
    abstraction--the function which do not have any return value or dont contain any info in the function all the implementstion is done from the parent or subclass
    recursion--the recursion is all about that we created a function and calling it inside the function
    arrays--the arrays are that contain lists or any info like numbers 1 -100 this can of three types 1d, 2d and 3d everyone ahve it's pwn functinality
    objects--the objects are the instance of classes to call the fnctions
    these concept are from oop which can be used from any proraming lang
    where as python is a dynamic language
    so there is many the langugae= uncluding pythobn etc
'''
# my name is moazzam riaz the student of university of lahore


def main():

    st.title("Document Query System")

    # Step 1: Initialize session state variables
    if 'username' not in st.session_state:
        st.session_state['username'] = None
    if 'login_successful' not in st.session_state:
        st.session_state['login_successful'] = False

    # Step 2: Check if user is logged in
    if st.session_state['username'] is None:
        # User is not logged in, display login and signup options
        selection = option_menu(
            menu_title="Main Menu",
            options=["Login", "Signup"],
            icons=["person", "person"],
            menu_icon="cast",
            default_index=1
        )

        if selection == "Login":
            st.session_state['username'] = login()
            if st.session_state['username']:
                st.session_state['login_successful'] = True
        elif selection == "Signup":
            signup()

    # Step 3: Check if user is logged in successfully
    if 'login_successful' in st.session_state and st.session_state['login_successful']:
        # User is logged in, display welcome message and query page
        if 'username' in st.session_state and st.session_state['username']:
            st.subheader(f"Welcome, {st.session_state['username']}!")
            run_query_app(st.session_state['username'])


if st.sidebar.button("Logout"):
    st.session_state['username'] = None
    st.session_state['login_successful'] = False
    st.empty()  # Clear the contents of the page

if __name__ == '__main__':
    main()
