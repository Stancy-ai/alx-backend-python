
# Unittest and Intergration Test

## Overview

This folder contains unit and integration tests for the `GithubOrgClient` class in your ALX Backend Python Testing projects. The tests ensure your GitHub client logic is correct, isolated, and reliable** without making real HTTP requests.



## 🧪 What is tested?

### 1️⃣ Unit Tests (`test_client.py`)

 `TestGithubOrgClient.test_org`:
  Tests that `.org` fetches organization data correctly using mocked `get_json`.

`TestGithubOrgClient.test_public_repos_url`:
 Tests that the `_public_repos_url` property extracts the correct URL from mocked `.org` data.

 `TestGithubOrgClient.test_public_repos`:
   Tests that `public_repos()` returns the expected list of repositories using mocked `_public_repos_url` and `get_json`.

`TestGithubOrgClient.test_has_license`:
   Tests the `has_license` static method for correctly identifying repository licenses using parameterized inputs.

---

### 2 Integration Tests (`test_integration_client.py`)

Uses `parameterized_class` with fixtures:

  * `org_payload`
  * `repos_payload`
  * `expected_repos`
  * `apache2_repos`

* Tests:

  * `test_public_repos`:
     Verifies `public_repos` retrieves the full repo list correctly.

  * `test_public_repos_with_license`:
     Verifies `public_repos` filters repositories by license correctly (e.g., `apache-2.0`).

All HTTP calls are *mocked using `requests.get` with `.json()` responses, ensuring no external calls are made during tests.

---

## 🛠️ How to run tests

Run all tests using:

```bash
python3 -m unittest discover
```

Or run a specific test file:

```bash
python3 -m unittest test_client.py
python3 -m unittest test_integration_client.py
```

Or using `pytest` for cleaner output:

```bash
pytest
```



