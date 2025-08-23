import React from 'react';

export default function CompanyCard({ company }) {
  return (
    <div className="bg-white rounded shadow p-4 flex items-center space-x-4">
      <img
        src={company.imageUrl}
        alt={company.name}
        className="w-16 h-16 rounded-full object-cover"
        loading="lazy"
      />
      <div>
        <h3 className="text-lg font-semibold">{company.name}</h3>
        <p className="text-gray-700">{company.title}</p>
      </div>
    </div>
  );
}
