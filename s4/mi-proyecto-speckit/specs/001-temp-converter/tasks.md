# Tasks: Conversor de Temperatura (Tkinter & CLI)

**Feature Branch**: `001-temp-converter`
**Input**: Design artifacts from `/specs/001-temp-converter/` (`spec.md`, `plan.md`, `data-model.md`, `contracts/`, `quickstart.md`)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization, dependency management with `uv` and package structure

- [X] T001 Configure Python 3.12 project structure, `pyproject.toml` with `uv`, and entry points in `pyproject.toml`
- [X] T002 [P] Create package module structure in `src/conversor/__init__.py` and test suite placeholder in `tests/__init__.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure and data structures that MUST be complete before ANY user story can be implemented

- [X] T003 Define `TemperatureScale` constants (`ABSOLUTE_ZERO = {"C": -273.15, "F": -459.67, "K": 0.0}`, `UNIDADES_VALIDAS = {"C", "F", "K"}`) and normalization function `normalizar_unidad()` in `src/conversor/core.py`
- [X] T004 [P] Setup base test runner suite and assertion helpers in `tests/test_converter.py`

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Conversión de temperaturas entre diferentes escalas (Priority: P1) 🎯 MVP

**Goal**: Implement mathematical conversions between Celsius, Fahrenheit and Kelvin using exact formulas without intermediate rounding: $C = (F - 32) \times \frac{5}{9}$, $F = C \times \frac{9}{5} + 32$, $K = C + 273.15$, $C = K - 273.15$, and combined $F \leftrightarrow K$ formulas. Format valid results with exactly two decimals and destination unit (e.g., `212.00 F`).

**Independent Test**: Run unit tests in `tests/test_converter.py` for references `0 C -> 32.00 F`, `32 F -> 0.00 C`, `0 C -> 273.15 K`, `273.15 K -> 0.00 C`, `32 F -> 273.15 K`, `273.15 K -> 32.00 F`, `100 C -> 212.00 F`, `-40 C -> -40.00 F`.

### Tests for User Story 1

- [X] T005 [P] [US1] Write unit tests for all inter-scale conversion formulas and verifiable references in `tests/test_converter.py`

### Implementation for User Story 1

- [X] T006 [US1] Implement `convertir_temperatura(valor: float, origen: str, destino: str) -> float` with exact composite formulas for $F \leftrightarrow K$ without intermediate rounding in `src/conversor/core.py`
- [X] T007 [US1] Implement `formatear_resultado(valor: float, unidad_destino: str) -> str` formatting with two decimals, handling `abs(valor) < 1e-9` as `0.0` to prevent `-0.00`, in `src/conversor/core.py`
- [X] T008 [US1] Implement conversion controller logic and Tkinter calculation trigger in `src/conversor/gui.py`

**Checkpoint**: At this point, User Story 1 (MVP) is fully functional and testable independently.

---

## Phase 4: User Story 2 - Conversión con misma unidad de origen y destino (Priority: P1)

**Goal**: Allow selecting identical source and target units (`C -> C`, `F -> F`, `K -> K`), preserving numeric value and applying two-decimal formatting (e.g., `25 C -> 25.00 C`, `-273.15 C -> -273.15 C`).

**Independent Test**: Run unit tests in `tests/test_converter.py` for identical unit conversions and verify output formatting with two decimals.

### Tests for User Story 2

- [X] T009 [P] [US2] Write unit tests for same-unit conversions (`C -> C`, `F -> F`, `K -> K`) in `tests/test_converter.py`

### Implementation for User Story 2

- [X] T010 [US2] Update `convertir_temperatura` in `src/conversor/core.py` to return the unmodified value when source and destination scales match.

**Checkpoint**: User Stories 1 AND 2 work independently and maintain consistent formatting.

---

## Phase 5: User Story 3 - Validación de límites físicos y cero absoluto (Priority: P1)

**Goal**: Reject inputs lower than absolute zero according to source unit: $C < -273.15$, $F < -459.67$, $K < 0$. Display `"Temperatura inferior al cero absoluto"` and prevent conversion output, while accepting exact boundary values ($-273.15$ C, $-459.67$ F, $0$ K).

**Independent Test**: Run unit tests in `tests/test_converter.py` verifying rejection of values strictly below absolute zero with exact message `"Temperatura inferior al cero absoluto"` and acceptance of exact boundary limits.

### Tests for User Story 3

- [X] T011 [P] [US3] Write unit tests for absolute zero limits and boundary checks in `tests/test_converter.py`

### Implementation for User Story 3

- [X] T012 [US3] Implement `validar_cero_absoluto(valor: float, unidad_origen: str) -> tuple[bool, str | None]` returning `(False, "Temperatura inferior al cero absoluto")` if below limit in `src/conversor/core.py`
- [X] T013 [US3] Integrate absolute zero validation into Tkinter GUI error display in `src/conversor/gui.py`

**Checkpoint**: Physical boundaries are protected across all conversions.

---

## Phase 6: User Story 4 - Validación y manejo de datos de entrada no válidos (Priority: P2)

**Goal**: Handle empty or spaces-only input displaying `"Ingrese una temperatura"` and non-numeric text displaying `"Ingrese un número válido"` without unhandled exceptions and without showing a conversion result.

**Independent Test**: Run unit tests in `tests/test_ui_logic.py` verifying error messages for empty, whitespace, and non-numeric inputs.

### Tests for User Story 4

- [X] T014 [P] [US4] Write unit tests for input validation (empty, spaces, alphanumeric text) in `tests/test_ui_logic.py`

### Implementation for User Story 4

- [X] T015 [US4] Implement `validar_entrada_temperatura(entrada: str | None) -> tuple[float | None, str | None]` in `src/conversor/core.py`
- [X] T016 [US4] Bind input validation to Tkinter entry widget and error label in `src/conversor/gui.py`

**Checkpoint**: All input anomalies are gracefully caught with exact spec error messages.

---

## Phase 7: User Story 5 - Conversiones sucesivas independientes sin persistencia de estados previos (Priority: P2)

**Goal**: Enable continuous conversions in both Tkinter GUI and CLI where error states or previous results do not linger or leak into subsequent operations.

**Independent Test**: Run tests in `tests/test_ui_logic.py` asserting that each conversion attempt clears previous results and sets only new output or error.

### Tests for User Story 5

- [X] T017 [P] [US5] Write state transition tests for consecutive conversions and error recovery in `tests/test_ui_logic.py`

### Implementation for User Story 5

- [X] T018 [US5] Implement `procesar_conversion(temp_str: str, origen_str: str, destino_str: str) -> tuple[bool, str]` in `src/conversor/core.py`
- [X] T019 [US5] Implement full interactive CLI loop and argument processing in `src/conversor/cli.py`
- [X] T020 [US5] Implement Tkinter state reset on every conversion action in `src/conversor/gui.py`

**Checkpoint**: Full independent lifecycle verified in GUI and CLI sessions.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Usability refinements, shortcuts and end-to-end validation

- [ ] T021 [P] Add package script entry points for `conversor` and `conversor-cli` in `pyproject.toml`
- [ ] T022 [P] Implement keyboard shortcut `<Return>` in Tkinter window in `src/conversor/gui.py`
- [ ] T023 Run full test suite validation via `uv run python -m unittest discover -s tests -p "test_*.py"`
- [ ] T024 Validate end-to-end scenarios per `quickstart.md` in PowerShell

---

## Dependencies & Execution Order

### Phase Dependencies
- **Setup (Phase 1)**: No dependencies — executes immediately.
- **Foundational (Phase 2)**: Depends on Phase 1 — BLOCKS all user stories.
- **User Stories (Phases 3 to 7)**: Depend on Phase 2 completion. Can proceed sequentially in priority order (`US1` -> `US2` -> `US3` -> `US4` -> `US5`) or in parallel for tasks marked `[P]`.
- **Polish (Phase 8)**: Depends on all user stories completed.

### Parallel Opportunities
- `T002` (module structure) can run in parallel with `T001`.
- `T004` (test scaffolding) can run in parallel with `T003`.
- Tests for each story (`T005`, `T009`, `T011`, `T014`, `T017`) can be created in parallel with their models/services.
- Polish tasks `T021` and `T022` can be executed in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)
1. Complete **Phase 1** (Setup).
2. Complete **Phase 2** (Foundational).
3. Complete **Phase 3** (User Story 1: Inter-scale math & two-decimal formatting).
4. Run tests for User Story 1 to validate MVP.

### Incremental Delivery
1. Foundation + US1 $\rightarrow$ Conversión básica funcional (MVP).
2. US2 $\rightarrow$ Soporte de conversión de misma unidad.
3. US3 $\rightarrow$ Protección estricta de cero absoluto y límites.
4. US4 $\rightarrow$ Manejo robusto de entradas vacías y alfanuméricas.
5. US5 $\rightarrow$ Sesiones continuas sin contaminación de estado en GUI y CLI.
6. Polish $\rightarrow$ Atajos de teclado y verificación completa.
