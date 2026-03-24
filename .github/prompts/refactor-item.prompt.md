# Refactor Item Type - Gilded Rose Kata

This prompt guides you through adding a new item type to the Gilded Rose inventory system using the Strategy Pattern.

## Step 1: Gather Requirements

**Item Name:** [Enter the name of the new item type, e.g., "Conjured Mana Cake"]

**Business Rules:** [Describe how this item's quality changes over time]
- How does quality change each day before sell-by date?
- How does quality change after sell-by date?
- Are there any quality limits (minimum/maximum)?
- Any special behaviors or thresholds?

## Step 2: Create Strategy Class

Create a new strategy class that implements the update logic for this item type.

### Python Example:
```python
class [ItemName]Strategy:
    def update(self, item):
        # Implement the business rules here
        item.sell_in -= 1
        # Add quality update logic based on business rules
        # Remember: quality should never go below 0 or above 50 (unless special)
```

### Key Implementation Points:
- Always decrement `sell_in` by 1
- Apply quality changes based on sell-by date status
- Use `max(0, quality)` to prevent negative quality
- Use `min(50, quality)` to cap quality (unless item is special like Sulfuras)
- Handle any special thresholds or behaviors

## Step 3: Register Strategy

Add the new strategy to the GildedRose class strategy mapping.

### Python Example:
```python
class GildedRose:
    STRATEGIES = {
        "Aged Brie": AgedBrieStrategy(),
        "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
        "Conjured Mana Cake": ConjuredStrategy(),
        "[ItemName]": [ItemName]Strategy(),  # Add your new strategy here
    }
```

## Step 4: Create Unit Tests

Create comprehensive unit tests covering all business rules and edge cases.

### Test Categories to Cover:
- Quality decrease/increase before sell-by date
- Quality decrease/increase after sell-by date
- Quality boundaries (never below 0, never above 50 unless special)
- Sell-in date behavior
- Any special thresholds or behaviors

### Python Example Test Structure:
```python
def test_[item_name_snake_case]_quality_[behavior_description](self):
    items = [Item("[ItemName]", initial_sell_in, initial_quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    self.assertEqual(expected_quality, items[0].quality)
    self.assertEqual(expected_sell_in, items[0].sell_in)
```

### Required Test Cases:
1. **Normal behavior before sell-by**: Test quality change when sell_in > 0
2. **Behavior after sell-by**: Test quality change when sell_in <= 0
3. **Quality minimum**: Test that quality never goes below 0
4. **Quality maximum**: Test that quality never goes above 50 (unless special)
5. **Sell-in decrement**: Test that sell_in always decreases by 1
6. **Edge cases**: Test boundary values (quality = 0, 1, 49, 50, etc.)

## Step 5: Run Tests and Refactor

1. Run all existing tests to ensure no regressions
2. Run your new tests to verify the implementation
3. Refactor the strategy implementation for clarity and maintainability
4. Consider extracting common logic if multiple strategies share patterns

## Step 6: Update Documentation

- Update any relevant documentation with the new item type
- Ensure the business rules are clearly documented
- Update examples or README files if necessary

## Common Patterns for Different Item Types:

- **Normal Items**: Quality decreases by 1 before sell-by, by 2 after
- **Aged Brie**: Quality increases by 1 before sell-by, by 2 after
- **Sulfuras**: Quality never changes (special case)
- **Backstage Passes**: Quality increases by 1 (sell_in > 10), 2 (5 < sell_in <= 10), 3 (0 < sell_in <= 5), 0 (sell_in <= 0)
- **Conjured Items**: Quality decreases twice as fast as normal items

## Validation Checklist:
- [ ] Strategy class created with correct update logic
- [ ] Strategy registered in GildedRose.STRATEGIES
- [ ] Unit tests cover all business rules
- [ ] Unit tests cover edge cases and boundaries
- [ ] All existing tests still pass
- [ ] Code follows language conventions and style
- [ ] Documentation updated if necessary</content>
<parameter name="filePath">/Users/macbookair/GildedRose-Refactoring-Kata/.github/prompts/refactor-item.prompt.md