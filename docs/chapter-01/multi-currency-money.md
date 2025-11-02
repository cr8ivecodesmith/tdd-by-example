# Multi-Currency Money Example


## Goal

Experience the TDD rythm while building a small multi-currency money library.


## TDD Rythm

1. Quickly add a test.
2. Run all tests and see the new one fail.
3. Make a little change.
4. Run all tests and see them pass.
5. Refactor to remove duplication.


## Behaviors

A multi-currency report should allow us to add amounts in different currencies
but total them in a single currency.

**Report example:**

| Instrument    | Shares    | Price    | Total        |
|---------------|-----------|----------|--------------|
| IBM           | 1000      | 25 USD   | 25000 USD    |
| Novartis      | 400       | 150 CHF  | 60000 CHF    |
|               |           | Total:   | 65000 USD    |

**Exchange rates:**

| From  | To    | Rate  |
|-------|-------|-------|
| CHF   | USD   | 1.5   |


**Calculations:**

```
$5 + 10 CHF = $10 if CHF to USD is 2:1
$5 * 2 = $10
```

- We need to be able to add amounts in two different currencies and convert the result given a set of exchange rates.
- We need to be able to multiply an amount (price per share) by a number (number of shares) and receive an amount.


## To-Do

- [ ] `$5 + 10 CHF = $10 if CHF to USD is 2:1`
- [ ] `$5 * 2 = $10`
- [ ] Make `amount` private
- [ ] Dollar side effects?
- [ ] Money rounding?

