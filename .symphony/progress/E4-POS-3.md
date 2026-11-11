# E4-POS-3 implementation progress

## Goal
Add the typed integer helper `clamp(value, low, high)` to `e4demo.mathutil`, with inclusive bounds, invalid-range rejection, and unit tests.

## Acceptance
- clamp returns low when value < low, high when value > high, and value otherwise.
- clamp raises ValueError when low > high.
- tests/test_mathutil.py has unit tests for all four cases and ./scripts/test.sh passes.
- ./scripts/test.sh

## Plan
1. In `tests/test_mathutil.py`, import `clamp` from `e4demo.mathutil` and add `MathUtilTest.test_clamp_below_range`, asserting `clamp(0, 1, 10) == 1`. Run `./scripts/test.sh` and record the expected missing-import failure. In `src/e4demo/mathutil.py`, add `clamp(value: int, low: int, high: int) -> int` after the existing helpers, implementing the lower-bound behavior needed for this first test. Re-run the suite and keep the existing tests enabled.
2. In `tests/test_mathutil.py`, add `MathUtilTest.test_clamp_inside_range`, asserting `clamp(5, 1, 10) == 5`. Observe it fail before updating `src/e4demo/mathutil.py`'s `clamp` to return `value` when it is not below `low`. In this test, also assert the inclusive endpoints `clamp(1, 1, 10) == 1` and `clamp(10, 1, 10) == 10`, and the valid single-point range `clamp(5, 5, 5) == 5`; verify these with the suite.
3. In `tests/test_mathutil.py`, add `MathUtilTest.test_clamp_above_range`, asserting `clamp(11, 1, 10) == 10`. Observe it fail, then update `src/e4demo/mathutil.py`'s `clamp` to return `high` when `value > high`. Re-run `./scripts/test.sh` to confirm all current cases pass.
4. In `tests/test_mathutil.py`, add `MathUtilTest.test_clamp_invalid_range`, using `self.assertRaises(ValueError)` around `clamp(5, 10, 1)`. Observe it fail, then update `src/e4demo/mathutil.py`'s `clamp` to check `low > high` before any clamping and raise `ValueError` with a concise explanation. Keep ordinary integer comparisons and returns, with no runtime type validation, dependencies, or changes to `add` or `is_even`. Re-run the suite.
5. Review only the changes to `src/e4demo/mathutil.py`'s `clamp` and the four new `MathUtilTest` methods in `tests/test_mathutil.py` for unnecessary complexity and preserved existing behavior. Run the final validation entrypoint in `scripts/test.sh` using `./scripts/test.sh`, then the top-level artifact entrypoint in `scripts/artifacts.sh` using `./scripts/artifacts.sh`; require both exit codes to be zero and record the actual results here. The harness defines no separate lint or typecheck command; do not introduce tooling or claim those checks ran. If the global heavy runner is available, wrap suite execution as `~/.agents/bin/heavy run -- ./scripts/test.sh`; exit 75 is a blocker to report, not a reason to retry in a loop.
6. Update `.symphony/progress/E4-POS-3.md` with observed test failures, final validation and artifact evidence, and any remaining limitations. Leave branching, commits, PRs, remote checks, merges, and tracker updates to Symphony. Do not change CI, README, other helpers, or the existing `.symphony/run_state.json`.

## Work Log
- Read the codebase and wrote the implementation plan.
- Planning turn only: no source or test changes made; tests and artifact generation have not been run in this turn.
- Implementation turn 1: added the four `MathUtilTest` clamp tests before adding the source helper. Assertions cover below, inside, above, invalid range, inclusive endpoints, and equal bounds.
- Implementation turn 1: added `clamp(value: int, low: int, high: int) -> int`, checking invalid bounds first, then the lower and upper limits, then returning an in-range value. Existing helpers and tests are unchanged.
- Reviewed the helper and tests for unnecessary complexity; no dependencies, fallback behavior, or unrelated changes were needed.
- The implementation-turn instructions supersede the plan's test execution steps: no test, full validation, smoke, build, or artifact command was run. Red/green execution was not observed. Symphony must run validation and artifact generation in its validation phase.

## Evidence
- `src/e4demo/mathutil.py`: contains a module docstring and the annotated `add(a: int, b: int) -> int` and `is_even(n: int) -> bool` helpers; `clamp` does not exist yet.
- `tests/test_mathutil.py`: uses standard-library `unittest`, imports `add` and `is_even` directly from the module, and groups assertions in `MathUtilTest`; extend this class without changing its existing tests.
- `scripts/test.sh`: changes to the repository root, sets `PYTHONPATH=src`, and executes `python3 -m unittest discover -s tests -v`; no extra test dependency is needed.
- `scripts/artifacts.sh`: changes to the repository root and emits a JSON snapshot containing the project name, count of test files, and current Git HEAD; it does not persist an artifact file.
- `.symphony/harness.yml`: identifies a Python library; validation, smoke, and post-merge all use `./scripts/test.sh`; artifacts use `./scripts/artifacts.sh`; behavioral proof is required in `unit_first` mode for `src/` changes with tests under `tests/`. No separate lint or typecheck command is configured.
- Repository inspection found no project `AGENTS.md` or `CLAUDE.md`. Initial `git status --short` showed only the pre-existing untracked `.symphony/run_state.json`; preserve it.

## Next Step
Implementation is complete. Symphony should run `./scripts/test.sh` and `./scripts/artifacts.sh` in the validation phase and record their actual results. No further implementation work is currently identified; tests, lint, and typecheck have not been executed in this implementation turn, and the harness specifies no separate lint or typecheck command.
