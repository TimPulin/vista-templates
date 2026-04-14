# 1. Objective

Create a formalized instruction set for an agent that builds an internal model based on:

* Existing files
* Identified syntax rules
* Recurring code patterns

---

# 2. Input Context

## 2.1 Structure

* A collection of independent files
* No explicit relationships (no imports/inheritance)

## 2.2 File Contents

Each file contains:

* HTML markup
* Embedded Python 2.7 code
* A templating syntax similar to Jinja2, but:
  * May differ in tags
  * May include custom constructs

---

# 3. Agent Core Task

The agent must:

1. Analyze existing files
2. Extract:
   * Templating constructs
   * Control structures
   * Recurring HTML blocks
3. Build an internal template model

---

# 4. Agent Workflow

## Step 1. Parsing

The agent must split files into blocks:

* HTML
* Python
* Template constructs

## Step 2. Syntax Identification

Determine:

* How variables are defined
* How loops are written
* How conditions are written

Examples (illustrative only):

* `{{ variable }}`
* `{% for item in list %}`
* `{% if condition %}`

**Important:** Do NOT assume Jinja2 — only capture actual syntax.

## Step 3. Pattern Extraction

The agent must detect recurring elements:

* Cards
* Tables
* Rows
* Conditional blocks

For each pattern, define:

* Inputs
* HTML structure
* Rendering conditions

## Step 4. Model Construction

Create an abstract representation:

```text
Component:
  name: string
  inputs: []
  structure: HTML + placeholders
  conditions: []
```

---

# 5. Model Output Requirements

The agent must produce a Markdown (`.md`) file containing a complete description of the constructed model.

## 5.1 Output File Constraints

* Format: `.md`
* The file must be self-contained
* No references to original files
* No executable code
* Only structured description of the model

## 5.2 Required Structure of the Output

The Markdown file must include the following sections:

### 1. Overview

* General description of the detected templating system
* Key characteristics of syntax and structure

### 2. Syntax Specification

Describe the identified syntax:

* Variable format
* Loop constructs
* Conditional constructs
* Any custom or non-standard elements

### 3. Components

For each detected component:

```text
Component: <name>
Inputs:
  - ...
Structure:
  - HTML/template structure
Conditions:
  - ...
```

### 4. Patterns

* List recurring patterns
* Describe their purpose
* Describe where and how they are used

### 5. Rules and Conventions

* Naming conventions
* Structural conventions
* Formatting rules
* Any implicit rules inferred from files

## 5.3 Quality Requirements

The generated Markdown must:

* Fully describe the model
* Be deterministic and unambiguous
* Be consistent across all sections
* Avoid duplication
* Reflect only observed patterns (no assumptions)

## 5.4 Validation

Before completion, the agent must ensure:

* All detected constructs are documented
* No undocumented syntax remains
* All components are described
* The structure is logically consistent

---

# 6. Machine-Readable Model (JSON)

In addition to the Markdown file, the agent must generate a JSON file representing the same model in a structured, machine-readable format.

## 6.1 Output Requirements

* Format: `.json`
* Must be fully aligned with the Markdown description
* No extra or missing data compared to the Markdown
* Deterministic structure

## 6.2 JSON Schema

The JSON file must follow this structure:

```json
{
  "syntax": {
    "variables": "string description",
    "loops": "string description",
    "conditions": "string description",
    "custom": ["string"]
  },
  "components": [
    {
      "name": "string",
      "inputs": ["string"],
      "structure": "string",
      "conditions": ["string"]
    }
  ],
  "patterns": [
    {
      "name": "string",
      "description": "string",
      "usage": "string"
    }
  ],
  "rules": {
    "naming": "string",
    "structure": "string",
    "formatting": "string",
    "other": ["string"]
  }
}
```

## 6.3 Consistency Rules

The agent must ensure:

* JSON and Markdown describe the same model
* Component names match exactly
* No additional interpretation in JSON
* No loss of detail when converting to JSON

## 6.4 Validation

Before completion, the agent must verify:

* JSON is valid
* Schema is respected
* All sections are filled
* Data is synchronized with Markdown

## 6.5 Output Artifacts

The agent must produce exactly two files:

* `model.md`
* `model.json`

Both files must be generated from the same internal model without divergence.