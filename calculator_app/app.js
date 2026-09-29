const expressionEl = document.getElementById('expression');
const resultEl = document.getElementById('result');

let currentExpression = '';
let lastResult = '0';

function isOperator(value) {
  return ['+', '-', '*', '/'].includes(value);
}

function formatResult(value) {
  if (!Number.isFinite(value)) {
    throw new Error('Division by zero is not allowed.');
  }

  return Number(value.toFixed(10)).toString();
}

function calculateExpression(expression) {
  const sanitized = expression.replace(/\s+/g, '');

  if (!sanitized) {
    throw new Error('Expression is empty.');
  }

  if (!/^[0-9+\-*/.]+$/.test(sanitized)) {
    throw new Error('Expression is invalid.');
  }

  if (/[+\-*/]$/.test(sanitized)) {
    throw new Error('Expression is invalid.');
  }

  if (sanitized.includes('..')) {
    throw new Error('Expression is invalid.');
  }

  const normalized = sanitized.replace(/(\d)\.(?!\d)/g, '$1.0');
  const result = Function(`"use strict"; return (${normalized});`)();

  if (!Number.isFinite(result)) {
    throw new Error('Division by zero is not allowed.');
  }

  return Number(result.toFixed(10));
}

function updateDisplay() {
  expressionEl.textContent = currentExpression || '0';
  resultEl.textContent = lastResult;
}

function appendValue(value) {
  if (value === '.') {
    const currentNumber = currentExpression.split(/[+\-*/]/).at(-1);
    if (currentNumber && currentNumber.includes('.')) {
      return;
    }

    if (!currentExpression || isOperator(currentExpression.slice(-1))) {
      currentExpression += '0.';
    } else {
      currentExpression += '.';
    }
    updateDisplay();
    return;
  }

  if (isOperator(value)) {
    if (!currentExpression && value !== '-') {
      return;
    }

    if (isOperator(currentExpression.slice(-1))) {
      currentExpression = currentExpression.slice(0, -1) + value;
    } else {
      currentExpression += value;
    }
    updateDisplay();
    return;
  }

  currentExpression += value;
  updateDisplay();
}

function clearExpression() {
  currentExpression = '';
  lastResult = '0';
  updateDisplay();
}

function deleteLast() {
  currentExpression = currentExpression.slice(0, -1);
  updateDisplay();
}

function evaluateCurrentExpression() {
  if (!currentExpression) {
    lastResult = '0';
    updateDisplay();
    return;
  }

  try {
    const result = calculateExpression(currentExpression);
    lastResult = formatResult(result);
    currentExpression = lastResult;
  } catch (error) {
    lastResult = error.message;
    currentExpression = '';
  }

  updateDisplay();
}

document.querySelectorAll('button').forEach((button) => {
  button.addEventListener('click', () => {
    const action = button.dataset.action;
    const value = button.dataset.value;

    if (action === 'clear') {
      clearExpression();
      return;
    }

    if (action === 'delete') {
      deleteLast();
      return;
    }

    if (action === 'equals') {
      evaluateCurrentExpression();
      return;
    }

    appendValue(value);
  });
});

updateDisplay();
