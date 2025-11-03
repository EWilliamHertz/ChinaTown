# Journal Update Guide

## How to Add New Entries to the Project Journal

This guide will help you add new journal entries to track progress, insights, and updates for the CT-Global project.

### Quick Steps

1. **Open the journal.html file** in your text editor
2. **Copy an existing journal entry block** (see template below)
3. **Paste it at the top** of the journal entries section
4. **Update the content** with your new information
5. **Save and push to GitHub**

### Journal Entry Template

Copy this template to create a new entry:

```html
<div class="journal-entry">
    <div class="journal-entry-header">
        <span class="journal-entry-date">Month Day, Year</span>
        <span class="text-sm text-gray-500">Category/Topic</span>
    </div>
    <div class="journal-entry-content">
        <h3 class="text-xl font-bold text-brand-blue mb-2">Entry Title</h3>
        <p class="mb-3">
            Your main content goes here. You can write paragraphs describing what happened,
            decisions made, or insights gained.
        </p>
        <ul class="list-disc ml-6 space-y-1">
            <li>Use bullet points for lists</li>
            <li>Keep items concise and clear</li>
            <li>Focus on key information</li>
        </ul>
        <p class="mt-3">
            <strong>Next Steps:</strong> Describe what comes next or action items.
        </p>
    </div>
</div>
```

### Where to Insert New Entries

1. Open `journal.html` in your text editor
2. Find this section (around line 100):
   ```html
   <!-- Sample Journal Entry 1 -->
   <div class="journal-entry">
   ```
3. **Paste your new entry ABOVE this line** so it appears first (most recent entries at the top)

### Formatting Tips

#### Date Format
```html
<span class="journal-entry-date">November 3, 2025</span>
```
Use the format: Month Day, Year

#### Category/Topic
```html
<span class="text-sm text-gray-500">Market Research</span>
```
Common categories:
- Website Updates
- Market Research
- Product Sourcing
- Supplier Negotiations
- Financial Planning
- Partnership Development
- Regulatory Compliance
- Technology Integration

#### Entry Title
```html
<h3 class="text-xl font-bold text-brand-blue mb-2">Your Title Here</h3>
```
Make it descriptive and action-oriented

#### Content Formatting

**Paragraphs:**
```html
<p class="mb-3">
    Your paragraph text here.
</p>
```

**Bullet Lists:**
```html
<ul class="list-disc ml-6 space-y-1">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ul>
```

**Bold Text:**
```html
<strong>Important text</strong>
```

**Next Steps Section:**
```html
<p class="mt-3">
    <strong>Next Steps:</strong> Describe your action items here.
</p>
```

### Example Entry

Here's a complete example:

```html
<div class="journal-entry">
    <div class="journal-entry-header">
        <span class="journal-entry-date">November 10, 2025</span>
        <span class="text-sm text-gray-500">Supplier Negotiations</span>
    </div>
    <div class="journal-entry-content">
        <h3 class="text-xl font-bold text-brand-blue mb-2">Initial Quotes Received from Chinese Manufacturers</h3>
        <p class="mb-3">
            Received formal quotes from 3 manufacturers on Alibaba for both unit types:
        </p>
        <ul class="list-disc ml-6 space-y-2">
            <li><strong>Manufacturer A:</strong> $1,850/unit for foldable, $6,500/unit for 40ft home (MOQ: 10 units)</li>
            <li><strong>Manufacturer B:</strong> $1,920/unit for foldable, $6,890/unit for 40ft home (MOQ: 5 units, better customization)</li>
            <li><strong>Manufacturer C:</strong> $1,780/unit for foldable, $6,200/unit for 40ft home (MOQ: 20 units)</li>
        </ul>
        <p class="mt-3">
            <strong>Next Steps:</strong> Schedule video calls with Manufacturer B and C to discuss customization options, 
            quality certifications, and shipping logistics. Request sample photos of completed projects.
        </p>
    </div>
</div>
```

### Publishing Your Changes

After adding your new entry:

1. **Save the file**
2. **Commit to Git:**
   ```bash
   git add journal.html
   git commit -m "Add journal entry: [Your Title]"
   ```
3. **Push to GitHub:**
   ```bash
   git push origin main
   ```

The changes will be live on your website within a few minutes.

### Best Practices

1. **Be Consistent:** Use the same date format and structure for all entries
2. **Be Concise:** Focus on key information and actionable insights
3. **Use Categories:** Help organize entries by topic
4. **Include Next Steps:** Always end with what comes next
5. **Regular Updates:** Add entries weekly or after major milestones
6. **Chronological Order:** Always add new entries at the top

### Troubleshooting

**Problem:** Entry doesn't display correctly
- **Solution:** Check that all HTML tags are properly closed (`<div>` has `</div>`, etc.)

**Problem:** Formatting looks wrong
- **Solution:** Make sure you copied the entire template including all CSS classes

**Problem:** Changes not showing on website
- **Solution:** Clear your browser cache or do a hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

### Need Help?

If you encounter issues:
1. Check that your HTML syntax is correct
2. Validate your HTML using an online validator
3. Compare your entry to the existing examples
4. Make sure all tags are properly nested and closed

---

**Remember:** The journal is a living document. Keep it updated regularly to track your project's progress and maintain a clear record of decisions and milestones.
