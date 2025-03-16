# Python_autotests
<h2>API test automation using Pytest and Requests</h2>

> **Project Status:**
> The project is closed for POST requests, but GET requests can be made without a token: https://pokemonbattle.ru/
>
>	🟢 Supported (Active)

## Project Description and Goals

Automate part of the regression testing using Pytest and Requests.

## Automated Test Cases
*  Creating a Pokémon: 'POST /pokemons'
*  Changing a Pokémon’s name: 'PUT /pokemons'
*  Catching a Pokémon in a Pokéball: 'POST /trainers/add_pokeball'
*  Verifying the response of the method: 'GET /trainers'

## Expected response:
*  Response 'status code' = 200
*  The response 'json' contains the correct field 'trainer_name'
*  The response JSON contains a valid id field

## Implementation Details
1. Autotests are written using Pytest
2. Requests library is used
3. Parameterized tests using decorators

## Local Test Execution (from Terminal)
1. Download the project
2. Navigate to the project directory in the terminal
3. Run the following commands:

Creating a virtual environment inside the project folder (for MacOS):

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```

4. Installing dependencies
``` markdown
python3 -m pip install requests
```
``` markdown
python3 -m pip install pytest
```

Running the tests
``` markdown
pytest tests/test_pokemon.py
```

5. Expected result: A test execution report will be generated.
