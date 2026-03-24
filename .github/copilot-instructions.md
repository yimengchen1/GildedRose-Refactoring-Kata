# Gilded Rose Refactoring Kata - Copilot Instructions

## Project Overview

The Gilded Rose Refactoring Kata is a coding exercise designed to practice refactoring skills and test-driven development. The repository contains implementations of the Gilded Rose inventory management system in multiple programming languages, each serving as a starting point for refactoring practice.

## Project Architecture

### Multi-Language Structure
- Each programming language has its own dedicated folder (e.g., `python/`, `java/`, `csharp/`, etc.)
- Language folders follow a consistent structure:
  - `src/` or language-specific source directory containing the main code
  - `test/` or language-specific test directory containing unit tests
  - `gilded_rose.*` - Main implementation file with `Item` class and `update_quality` method
  - `texttest_fixture.*` - Command-line program for TextTest approval testing
  - `README.md` - Language-specific setup and running instructions

### Core Components
- **Item Class**: Represents inventory items with `name`, `sell_in`, and `quality` properties
- **GildedRose Class**: Contains the `update_quality()` method that processes all items daily
- **Strategy Pattern**: Different item types (Normal, Aged Brie, Sulfuras, Backstage Passes, Conjured) use different update strategies

### Business Rules (from GildedRoseRequirements.md)
- Items degrade in quality over time
- Quality degrades twice as fast after sell-by date
- Quality never goes below 0 or above 50 (except Sulfuras at 80)
- Special items have unique behaviors:
  - Aged Brie increases in quality
  - Sulfuras never changes
  - Backstage passes increase quality faster as concert approaches, then drop to 0
  - Conjured items degrade twice as fast as normal items

## Coding Standards

### General Guidelines
- **Do not alter the Item class** - It belongs to a "goblin in the corner" who doesn't believe in shared code ownership
- Focus on refactoring the `update_quality` method and related logic
- Practice incremental changes with frequent testing
- Use the strategy pattern or similar design patterns to handle different item types

### File Naming Conventions
- Main implementation: `gilded_rose` (with appropriate language extension and casing)
- Unit tests: `gilded_rose_test` or similar
- TextTest fixture: `texttest_fixture` or `program`

### Starting Position Requirements
- Include one failing unit test that expects "fixme" != "foo" to encourage test understanding
- Keep the starting position minimal to avoid spoiling the exercise
- Provide a TextTest fixture for approval testing when possible

## Testing Approach

### Unit Testing
- Use the language's popular unit testing framework (unittest for Python, JUnit for Java, etc.)
- Start with the provided failing test and expand coverage incrementally
- Test all business rules from the requirements specification
- Focus on edge cases: quality boundaries, sell-in dates, special item behaviors

### Approval Testing
- **TextTest**: Command-line approval testing tool
  - Run `texttest_fixture` with number of days to simulate
  - Compare output against approved text files
  - Use for comprehensive regression testing
- **ApprovalTests Framework**: Available for some languages
  - Generates and approves output files
  - Useful for testing complex output scenarios

### Testing Strategy
1. **Start with existing tests** - Ensure they pass before refactoring
2. **Add comprehensive unit tests** - Cover all requirements and edge cases
3. **Use approval tests** - For validating overall system behavior
4. **Refactor incrementally** - Make small changes, run tests frequently
5. **Test special cases** - Quality limits, sell-in date boundaries, item type behaviors

### Test Categories
- Normal item degradation (before and after sell-by)
- Aged Brie quality increase
- Sulfuras immutability
- Backstage pass quality progression and expiration
- Conjured item double degradation
- Quality boundary conditions (0, 50, 80 for Sulfuras)

## Development Workflow

1. Choose a language implementation folder
2. Set up the development environment (virtual environment, dependencies)
3. Run existing tests to ensure they pass
4. Study the requirements and understand current code behavior
5. Add comprehensive unit tests covering all scenarios
6. Refactor the code incrementally while maintaining test coverage
7. Use approval tests to validate overall system behavior
8. Focus on clean code principles: single responsibility, open/closed principle, etc.

## Key Principles

- **Legacy Code Mindset**: Treat the starting code as inherited legacy code
- **Test-First**: Write tests before making changes
- **Incremental Refactoring**: Small, safe steps with constant validation
- **Multiple Testing Approaches**: Combine unit tests with approval tests
- **Language Agnostic**: Core concepts apply across all language implementations

This kata emphasizes practical refactoring skills, test design, and maintaining system behavior while improving code quality.</content>
<parameter name="filePath">/Users/macbookair/GildedRose-Refactoring-Kata/.github/copilot-instructions.md