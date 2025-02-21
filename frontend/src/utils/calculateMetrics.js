export const calculateMetrics = (data, column) => {
    if (!data || !column || data.length === 0) return null;
  
    const values = data.map((item) => parseFloat(item[column])).filter((val) => !isNaN(val));
    if (values.length === 0) return null;
  
    const mean = values.reduce((sum, val) => sum + val, 0) / values.length;
    const sortedValues = [...values].sort((a, b) => a - b);
    const median = sortedValues.length % 2 === 0
      ? (sortedValues[sortedValues.length / 2 - 1] + sortedValues[sortedValues.length / 2]) / 2
      : sortedValues[Math.floor(sortedValues.length / 2)];
  
    const stdDev = Math.sqrt(values.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / values.length);
  
    const growthRate = values.length > 1
      ? ((values[values.length - 1] - values[0]) / values[0]) * 100
      : 0;
  
    return {
      mean: mean.toFixed(2),
      median: median.toFixed(2),
      stdDev: stdDev.toFixed(2),
      growthRate: growthRate.toFixed(2),
    };
  };
  