import React from 'react';

export const Button = ({ children, variant = 'default', className = '', ...props }) => {
  const baseStyles = 'px-4 py-2 rounded font-medium transition-colors';
  const variants = {
    default: 'bg-blue-500 text-white hover:bg-blue-600',
    outline: 'border border-gray-300 hover:bg-gray-50',
    destructive: 'bg-red-500 text-white hover:bg-red-600',
  };
  
  return (
    <button 
      className={`${baseStyles} ${variants[variant]} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
};

export const Input = ({ className = '', ...props }) => {
  return (
    <input 
      className={`w-full px-3 py-2 border rounded ${className}`}
      {...props}
    />
  );
};

export const Label = ({ children, className = '', ...props }) => {
  return (
    <label className={`block text-sm font-medium mb-1 ${className}`} {...props}>
      {children}
    </label>
  );
};

export const Switch = ({ checked, onCheckedChange, ...props }) => {
  return (
    <button
      onClick={() => onCheckedChange(!checked)}
      className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${
        checked ? 'bg-blue-500' : 'bg-gray-300'
      }`}
      {...props}
    >
      <span
        className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
          checked ? 'translate-x-6' : 'translate-x-1'
        }`}
      />
    </button>
  );
};

export const Select = ({ children, className = '', ...props }) => {
  return (
    <select className={`w-full px-3 py-2 border rounded ${className}`} {...props}>
      {children}
    </select>
  );
};

export const SelectTrigger = ({ children, ...props }) => {
  return <div {...props}>{children}</div>;
};

export const SelectValue = ({ placeholder }) => {
  return <span>{placeholder}</span>;
};

export const SelectContent = ({ children }) => {
  return <div>{children}</div>;
};

export const SelectItem = ({ children, value, ...props }) => {
  return <option value={value} {...props}>{children}</option>;
};
