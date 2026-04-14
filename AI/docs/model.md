# 1. Overview

The detected templating model is a mixed HTML + embedded Python rendering system with explicit control directives inside braces.  
The dominant syntax uses single-brace directives and expressions, where Python execution, branching, and iteration are embedded directly in the markup flow.

Key characteristics:

- HTML acts as the primary layout layer.
- Python 2.7-style statements are embedded through dedicated directive blocks.
- Control flow is explicit and block-based (`if` / `elif` / `else` / `end`, `for` / `end`).
- Dynamic values are interpolated inline using brace expressions.
- A secondary variable interpolation style with double braces also appears in a small subset of templates.

# 2. Syntax Specification

## Variable format

- Main interpolation: `{expression}`
- Main interpolation with output modifier: `{expression:n}`
- Secondary interpolation: `{{expression}}`

## Loop constructs

- Iteration: `{for: item in collection}`
- Loop closure: `{end:}`

## Conditional constructs

- Condition start: `{if: condition}`
- Alternative branch: `{elif: condition}`
- Fallback branch: `{else:}`
- Block closure: `{end:}`

## Custom or non-standard elements

- Python execution block: `{: python_statement}`
- Multiline Python block: `{:` followed by multiple Python lines and closed by `}`
- Render/page setup directives called as expressions in braces (for example page size, margins, orientation)
- Inline output modifier suffix `:n` inside expression placeholders

# 3. Components

Component: DocumentShell
Inputs:
  - Page parameters (size, orientation, margins)
  - Document metadata values (titles, organisation labels, dates)
Structure:
  - Root HTML skeleton with `<html>`, `<head>`, `<body>`
  - Print-oriented style blocks and top-level document headers
  - Placeholder-based insertion points for dynamic textual fields
Conditions:
  - Optional header fragments rendered only when source values exist

Component: DataBootstrap
Inputs:
  - Runtime context objects (event/action/client/context)
  - Database handles and query results
  - Derived temporary variables
Structure:
  - Early template section with Python imports and assignments
  - Query execution and normalization into intermediate variables
  - Prepared values consumed by later HTML blocks
Conditions:
  - Query result checks before value extraction
  - Fallback assignments for absent data

Component: ConditionalContentBlock
Inputs:
  - Boolean conditions from runtime context
  - Primary and fallback text/value variants
Structure:
  - Inline or multiline branching segments embedded in HTML
  - `if`/`elif`/`else` paths selecting fragments, labels, and placeholders
Conditions:
  - Business-status checks
  - Existence checks for optional properties
  - Type/value checks for alternative render branches

Component: RepeatingTableRows
Inputs:
  - Collection variables (lists, query-derived rows, action sets)
  - Per-item fields used in cells
Structure:
  - Table wrapper (`<table>`, `<thead>`, `<tbody>`)
  - Row template repeated inside `{for: ...}` blocks
  - Cell-level placeholders for item fields
Conditions:
  - Optional row sections controlled by nested conditions
  - Empty-value fallbacks within repeated rows

Component: CardAndSignatureBlock
Inputs:
  - Person names, posts, dates, and contact data
  - Optional signature-related fields
Structure:
  - Bordered/card-like containers for highlighted instructions or summaries
  - Footer/signature rows with aligned labels and dynamic identity fields
Conditions:
  - Signature role selection when multiple sources are possible
  - Conditional display of optional sign-off lines

# 4. Patterns

- Card pattern  
  Purpose: highlight instruction or summary content in visually separated boxed sections.  
  Usage: appears as bordered containers with grouped text and list elements near informational or final sections.

- Table pattern  
  Purpose: present structured medical or administrative data in fixed columns.  
  Usage: repeated across templates for registers, lists, and tabular records with explicit widths and print styles.

- Repeated row pattern  
  Purpose: render variable-length collections.  
  Usage: `for` blocks generate `<tr>` sequences and inject per-item fields into cells.

- Conditional fallback pattern  
  Purpose: keep document output complete when fields are missing or states differ.  
  Usage: `if`/`elif`/`else` chains select concrete values, placeholders, or alternative wording.

- Bootstrap-then-render pattern  
  Purpose: separate data preparation from markup rendering.  
  Usage: early Python blocks compute variables first; later HTML sections consume prepared values.

# 5. Rules and Conventions

- Naming conventions
  - Temporary variables are commonly snake_case.
  - Context-bound fields use dotted access (`object.field`) and indexed property access (`object[u'Field']`).
  - Component-like sections are named by semantic purpose (header, table, signature, summary).

- Structural conventions
  - Control blocks are always explicitly closed with `{end:}`.
  - Data preparation blocks generally precede dependent HTML sections.
  - Nested conditions and loops are embedded directly within surrounding HTML.

- Formatting rules
  - Print-centric inline styling and explicit table geometry are common.
  - Dynamic placeholders are kept close to visible labels.
  - Optional text often uses inline conditional blocks to preserve layout.

- Other inferred rules
  - The same directive grammar is reused across many independent templates.
  - Secondary `{{...}}` interpolation is isolated and does not replace the primary brace directive model.
# 1. Overview

The detected templating environment is hybrid and supports multiple coexisting syntax dialects inside HTML documents. The dominant rendering flow is server-side generation with embedded Python-style expressions and control directives.

Key characteristics:
- HTML is used as the base layout layer.
- Template constructs are embedded inline in text nodes and attributes.
- Control flow is expressed directly in template tags.
- Python-like expressions, unicode literals, and helper calls are used in template logic.
- Reusable rendering is built around repeated sections, table rows, and conditional field blocks.

# 2. Syntax Specification

## 2.1 Variable Format

- Double-brace output interpolation: `{{ expression }}`
- Single-brace output interpolation: `{expression}`
- Plus-placeholder interpolation: `[[+placeholder_name]]`

Observed expression style:
- Dot access: `context.client_fio`
- Index access: `action[u'Field Name']`
- Mixed expression logic: fallback values, conditional expressions, method calls

## 2.2 Loop Constructs

- Block loop with percent tags:
  - Start: `{% for item in collection %}`
  - End: `{% endfor %}`
- Block loop with colon tags:
  - Start: `{for: item in collection}` or `{for: a, b in collection}`
  - End: `{end:}`

## 2.3 Conditional Constructs

- Block condition with percent tags:
  - Start: `{% if condition %}`
  - Optional branch: `{% else %}`
  - End: `{% endif %}`
- Block condition with colon tags:
  - Start: `{if: condition}`
  - End: `{end:}`

## 2.4 Custom / Non-Standard Elements

- Inline statement directive: `{: statement }`
- Multiline statement block:
  - Start: `{:`
  - Body: Python-like statements
  - End: `}`
- Assignment in template logic via statement directive.
- Function definition inside template statement blocks.
- Mixed usage of template variables inside HTML attributes and body text.

# 3. Components

Component: DocumentHeader
Inputs:
  - person_name
  - document_id
  - document_date
Structure:
  - Header container with centered title lines and identity fields
  - Inline placeholders for identity and date attributes
Conditions:
  - Optional lines rendered only when source values exist

Component: PrimaryAssessmentSection
Inputs:
  - first_act
  - is_deciduous
Structure:
  - Section title, examination date, and grouped descriptive fields
  - Nested conditional text blocks for alternate wording
Conditions:
  - Entire section may be guarded by date presence
  - Sub-blocks vary by boolean flags

Component: TeethFormulaTable
Inputs:
  - top_teeth_list
  - bottom_teeth_list
  - teeth_data_map
Structure:
  - Multi-row table with repeated cells for top and bottom arcs
  - Rows for status, mobility, condition, and tooth index
Conditions:
  - Cell fallback logic for missing tooth data
  - Loop-driven row generation over both arcs

Component: SecondaryAssessmentSection
Inputs:
  - second_acts_list
Structure:
  - Repeated section per act with title, date, diagnosis, treatment fields
  - Label-value lines rendered in sequence
Conditions:
  - Field-level conditional blocks for optional attributes
  - Section repetition by loop over acts

Component: ServicesTable
Inputs:
  - services_list
  - total_sum
Structure:
  - Table with service code, name, price, quantity, amount
  - Footer row for aggregate total
Conditions:
  - Optional fallback values when fields are empty
  - Loop-generated service rows

Component: StructuredGridForm
Inputs:
  - scalar_fields
  - person_blocks
  - monetary_fields
Structure:
  - Fixed-width grid layout with boxed cells and separators
  - Cells filled via helper rendering functions
  - Repeated mini-rows for personal data triplets and date segments
Conditions:
  - Some fields rendered with explicit empty placeholders
  - Numeric values split into major/minor parts before rendering

Component: PropertyMatrix
Inputs:
  - property_groups
  - action_map
Structure:
  - Nested table composition with repeated property lines
  - Label, value, and unit triplets per row
Conditions:
  - Rows filtered by membership checks
  - Reusable property list assignments drive loop rendering

Component: MediaSidebarBlock
Inputs:
  - title_placeholder
  - date_placeholder
Structure:
  - Repeated media cards with iframe/image and descriptive text
  - Placeholder injection in attributes and captions
Conditions:
  - Optional date placeholder rendering per media item

# 4. Patterns

- Header identity block:
  - Purpose: show key person/document metadata at the top.
  - Usage: fixed heading area with inline placeholders.

- Section card pattern:
  - Purpose: group related medical or form data into readable blocks.
  - Usage: repeated `<section>` or `<div>` containers with local conditions.

- Table row repeater:
  - Purpose: render homogeneous records such as services, properties, or measurements.
  - Usage: loops generating `<tr>` lines from a list/map.

- Conditional field line:
  - Purpose: avoid printing empty clinical or administrative fields.
  - Usage: if-block around a single label-value line.

- Grid cell writer pattern:
  - Purpose: print strict form layouts with character-level padding.
  - Usage: helper calls from statement directives writing normalized cells.

- Precomputed list pattern:
  - Purpose: centralize repeated display configuration (labels, units, key lists).
  - Usage: assignment directives that feed subsequent loops and filters.

# 5. Rules and Conventions

- Naming conventions:
  - Context roots typically use semantic names such as `context`, `action`, `client`, `service`.
  - Field identifiers combine snake_case and camelCase depending on data source.
  - Temporary loop variables are short and domain-specific (`item`, `prop`, `service`, `tooth_num`).

- Structural conventions:
  - HTML remains the primary structure; template directives are embedded and minimal per line.
  - Repetition is usually implemented at row/section granularity, not whole-document duplication.
  - Optional data is controlled by explicit conditions near output location.

- Formatting rules:
  - Directive tags are separated from HTML for readability.
  - Fallback values are defined inline in output expressions.
  - Data-heavy forms rely on helper functions for consistent width and alignment.

- Other inferred rules:
  - Template logic allows Python-style expressions and unicode string literals.
  - Both interpolation-only and statement-capable directives are supported.
  - Different syntax dialects can appear in the same repository, implying multi-engine compatibility.
