import React from 'react';

export default function DriverCard({ driver, assignedTruck, company }) {
  return (
    <div className="bg-white rounded shadow p-3 flex items-center space-x-4">
      <img
        src={driver.imageUrl}
        alt={driver.name}
        className="w-16 h-16 rounded-full object-cover"
        loading="lazy"
      />
      <div className="flex-1">
        <h3 className="text-lg font-semibold">{driver.name}</h3>
        <p className="text-gray-600">Company: {company?.name || "N/A"}</p>
        <p className="text-gray-600">
          Assigned Truck: {assignedTruck ? assignedTruck.name : "None"}
        </p>
      </div>
    </div>
  );
}
