# Inversion of Control Example

Demonstrates the utilization of the Onion Architecture and the Repository and Inversion of Control design patterns in a web application.

## Setup

1. Install dependencies using `Poetry`:

   ```bash
   poetry install
   ```

1. Copy the `.env.example` file next to it and rename it to `.env`. Adapt the parameters if needed.

   ```bash
   cp snaking/.env.example snaking/.env
   ```

## Running the application

1. Activate poetry shell

    ```bash
    poetry shell
    ```

1. Run the application manually, or using the example VSCode launch file.

   ```bash
   hypercorn snaking.app:app --reload --bind="localhost:8000" --log-level=debug
   ```

## Testing

1. Comment out all entries from the `.env` file, or remove it completely, because it overwrites the mocked configuration used by the tests.
1. Activate poetry shell

    ```bash
    poetry shell
    ```

1. Run `pytest` on `testing/tests`.

   ```bash
   pytest testing/tests/
   ```
