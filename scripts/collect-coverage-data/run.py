import pandas as pd
import requests
from .models.repository import Repository
from .wrappers import RepositoryWrapper, ProjectWrapper

# Helper functions


def get_readme(repo, default_branch):
    url = f'https://github.com/{repo}/blob/{default_branch}/README.md'
    response = requests.get(url)
    return response.text


def get_codecov_data(repo):
    # Call Codecov API
    pass


def get_coveralls_data(repo):
    # Call Coveralls API
    pass


def get_codeclimate_data(repo):
    # Call Coveralls API
    pass


index = 0
for project in ProjectWrapper.list():
    index += 1
    found = False
    has_codecov = 0
    has_coveralls = 0
    has_codeclimate = 0

    repo = project['name']
    language = project['mainLanguage']
    default_branch = project['defaultBranch']
    # print(repo, language)
    read_me = get_readme(repo, default_branch)

    # Check for Codecov badge
    codecov_string = f'codecov.io'
    if codecov_string in read_me:
        found = True
        data = get_codecov_data(repo)
        print(f"{repo} has Codecov data: {data}")
        has_codecov = 1

    # Check for Coveralls badge
    coveralls_string = f'coveralls.io'
    if coveralls_string in read_me:
        found = True
        data = get_coveralls_data(repo)
        print(f"{repo} has Coveralls data: {data}")
        has_coveralls = 1

    # Check for Code Climate badge
    codeclimate_string = "codeclimate.com"
    if codeclimate_string in read_me:
        found = True
        data = get_codeclimate_data(repo)
        print(f"{repo} has Code Climate data: {data}")
        has_codeclimate = 1

    if found:
        repository = Repository(name=repo,
                                language=language,
                                default_branch=str(default_branch),
                                has_codecov=has_codecov,
                                has_coveralls=has_coveralls,
                                has_codeclimate=has_codeclimate)
        RepositoryWrapper.create(repository)
        print("created!")
    if index == 100:
        break
