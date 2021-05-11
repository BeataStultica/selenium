from behave import *


@given("The Github page is displayed")
def step_impl(context):
    context.github_po.get_github()


@when('I have entered "{text}" in github search')
def step_impl(context, text):
    context.github_po.search(text)


@then('tags contains "{tag1}", "{tag2}" and "{tag3}"')
def step_impl(context, tag1, tag2, tag3):
    tags = context.github_po.tags()
    assert tag1 in tags and tag2 in tags and tag3 in tags


@given("click the star")
def step_impl(context):
    context.github_po.star_click()


@when('title is "{title}"')
def step_impl(context, title):
    assert context.github_po.get_title() == title


@step('I enter the "{login}" and "{password}"')
def step_impl(context, login, password):
    context.github_po.sign_in(login, password)


@then('error contain "{error}"')
def step_impl(context, error):
    assert context.github_po.get_after_login_error() == error



