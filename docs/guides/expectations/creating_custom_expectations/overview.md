---
title: Overview
---
import Prerequisites from './components/prerequisites.jsx'

You can extend the functionality of Great Expectations by creating your own custom [**Expectations**](../../../reference/expectations/expectations.md). You can also enrich Great Expectations as a shared standard for data quality by contributing new Expectations to the open source project.

These processes compliment each other and their steps are streamlined so that one flows into the other. Once you have created a custom Expectation, it is simple to contribute it to the open source project. This section will teach you how to do both.

<Prerequisites></Prerequisites>

## Steps to create a custom Expectation

A fully-developed, Production-ready Expectation needs to do a lot of things:
* Execute consistently across many types of data infrastructure
* Render itself and its Validation Results into several formats
* Support Profiling against new data
* Be maintainable, with good tests, documentation, linting, type hints, etc.

In order to make development of Expectations as easy as possible, we've broken up the steps to create custom Expectations into a series of bite-sized steps. Each step can be completed in minutes. They can be completed (and contributed) incrementally, unlocking value at each step along the way.

Grouped together, they constitute a Definition of Done for Expectations at each [Level of Maturity](../../../contributing/contributing_maturity.md).

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer"/>
<i class="fas fa-circle" style={{color: "#dc3545"}}></i> An Experimental Expectation...

* Has a `library_metadata` object
* Has a docstring, including a one-line short description
* Has at least one positive and negative example case
* Has core logic and passes tests on at least one [**Execution Engine**](../../../reference/execution_engine.md)

<i class="fas fa-circle" style={{color: "#ffc107"}}></i> A Beta Expectation...

* Has basic input validation and type checking
* Has all four Statement Renderers: question, descriptive, prescriptive, diagnostic
<!-- * Has default `Parameter Builders` and Domain hooks to support Profiling -->
* Has core logic that passes tests for all applicable Execution Engines and SQL dialects

<i class="fas fa-check-circle" style={{color: "#28a745"}}></i> A Production Expectation...

* Passes all linting checks
<!--  * Has all applicable Renderers, with fully typed and styled output -->
* Has a full suite of tests, as determined by project code standards
* Has passed a manual review by a code owner for code standards and style guides

## How these docs are organized

The docs in `Creating Custom Expectations` focus on completing the four steps for Experimental Expectations. Completing them will get to the point where your Expectation can be executed against one backend, with a couple tests to verify correctness, and a basic docstring and metadata to support diagonstics. Optionally, you can also publish experimental Expectations to the [Great Expectations open source gallery](https://greatexpectations.io/expectations) by following the steps [here](overview.md#publishing-your-expectation-as-an-open-source-contribution).

The code to achieve the first four steps looks somewhat different depending on the class of Expectation you're developing. Accordingly, there are separate how-to guides and templates for each class of Expectation.

| Guide: "How to create a custom..." |  Template |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Column Map Expectation](how_to_create_custom_column_map_expectations.md)             | [column_map_expectation_template](https://github.com/great-expectations/great_expectations/blob/develop/examples/expectations/column_map_expectation_template.py)       |
| [Column Aggregate Expectation](how_to_create_custom_column_aggregate_expectations.md) | [column_aggregate_expectation_template](https://github.com/great-expectations/great_expectations/blob/develop/examples/expectations/column_map_expectation_template.py) |

:::note 
Not all classes of Expectation currently have guides and templates. <br></br>
If you'd like to develop a different kind of Expectation, please reach out on [Slack](https://greatexpectations.io/slack).
:::

Beyond the first four steps, additional features are generally similar across all Expectation classes. Accordingly, each of the remaining steps has its own how-to guide in the `Adding Features to Custom Expectations` section of the table of contents.

| Step | Guide |
|------|-------|
| Has basic input validation and type checking                                                     | [How to add configuration validation for an Expectation](../features_custom_expectations/how_to_add_input_validation_for_an_expectation.md) |
| Has all four Statement Renderers: question, descriptive, prescriptive, diagnostic              | [How to add text renderers for custom Expectations](../features_custom_expectations/how_to_add_text_renderers_for_an_expectation.md) |
| Has core logic that passes tests for all applicable Execution Engines and SQL dialects   | [How to add SQLAlchemy support for custom Metrics](../features_custom_expectations/how_to_add_sqlalchemy_support_for_an_expectation.md)<br/> [How to add Spark support for custom Metrics](../features_custom_expectations/how_to_add_spark_support_for_an_expectation.md)|
| Passes all linting checks                                                                        | |
| Has a full suite of tests, as determined by project code standards                               | |
| Has passed a manual review by a code owner for code standards and style guides                   | |

## Publishing your Expectation as an open source contribution

You can find more detailed instructions in the [Contributing](../../../contributing/contributing.md) section of the docs.

## Wrapping up