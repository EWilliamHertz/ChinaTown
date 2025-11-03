// Project Planner Cost Calculator

const regionCostMultipliers = {
    'kenya': {
        'land': 1.0,
        'site': 1.0,
        'foundation': 1.0,
        'trenching': 1.0,
        'unit': 1.0,
        'shipping': 1.0,
        'lastmile': 1.0,
        'surveillance': 1.0,
        'wifi': 1.0,
        'meters': 1.0,
        'solar': 1.0,
        'permits': 1.0,
        'notes': 'kenya'
    },
    'nigeria': {
        'land': 1.2,
        'site': 1.1,
        'foundation': 1.15,
        'trenching': 1.1,
        'unit': 1.0,
        'shipping': 1.15,
        'lastmile': 1.3,
        'surveillance': 1.05,
        'wifi': 1.1,
        'meters': 1.1,
        'solar': 1.1,
        'permits': 1.4,
        'notes': 'nigeria'
    },
    'albania': {
        'land': 1.5,
        'site': 0.9,
        'foundation': 0.85,
        'trenching': 0.85,
        'unit': 1.0,
        'shipping': 0.6,
        'lastmile': 0.7,
        'surveillance': 0.9,
        'wifi': 0.9,
        'meters': 0.95,
        'solar': 0.95,
        'permits': 0.8,
        'notes': 'albania'
    }
};

function initializePlanner() {
    const table = document.getElementById('budget-table');
    const regionSelect = document.getElementById('region-select');
    
    if (!table || !regionSelect) {
        console.log('Planner elements not found on this page');
        return;
    }

    // Function to update all costs
    function updateCosts() {
        const selectedRegion = regionSelect.value;
        const multipliers = regionCostMultipliers[selectedRegion];
        
        let subtotal = 0;

        // Iterate over each data cell in the table
        table.querySelectorAll('td[data-cost-total]').forEach(cell => {
            const item = cell.getAttribute('data-item');
            const baseTotal = parseFloat(cell.getAttribute('data-cost-total'));
            const baseUnit = cell.getAttribute('data-cost-unit');
            
            let newTotal = baseTotal;
            let newUnit = baseUnit;

            // Apply multipliers for specific items
            if (multipliers[item]) {
                newTotal = baseTotal * multipliers[item];
                if (baseUnit !== '-') {
                    newUnit = parseFloat(baseUnit) * multipliers[item];
                }
            }

            // Add to subtotal (exclude contingency for now)
            if (item !== 'contingency') {
                subtotal += newTotal;
            }

            // Update the table cells
            const totalCell = document.getElementById(`cost-${item}`);
            const unitCell = totalCell.previousElementSibling;

            totalCell.textContent = '$' + newTotal.toLocaleString('en-US', { maximumFractionDigits: 0 });
            if (newUnit !== '-') {
                unitCell.textContent = '$' + newUnit.toLocaleString('en-US', { maximumFractionDigits: 0 });
            }
        });

        // Update Contingency
        const contingencyCell = document.getElementById('cost-contingency');
        const newContingency = subtotal * 0.20;
        contingencyCell.textContent = '$' + newContingency.toLocaleString('en-US', { maximumFractionDigits: 0 });

        // Update Total
        const totalCell = document.getElementById('cost-total');
        const newTotal = subtotal + newContingency;
        totalCell.textContent = '$' + newTotal.toLocaleString('en-US', { maximumFractionDigits: 0 });

        // Update Notes
        table.querySelectorAll('td[data-notes]').forEach(noteCell => {
            if (noteCell.getAttribute('data-notes') === multipliers.notes) {
                noteCell.classList.remove('hidden');
            } else {
                noteCell.classList.add('hidden');
            }
        });
    }

    // Add event listener
    regionSelect.addEventListener('change', updateCosts);

    // Run once on load
    updateCosts();
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializePlanner);
} else {
    initializePlanner();
}
