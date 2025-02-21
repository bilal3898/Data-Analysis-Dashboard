export const formatDate = (dateString) => {
    if (!dateString) return "N/A";
  
    const date = new Date(dateString);
    if (isNaN(date)) return "Invalid Date";
  
    return date.toLocaleDateString("en-US", {
      day: "2-digit",
      month: "short",
      year: "numeric",
    });
  };
  