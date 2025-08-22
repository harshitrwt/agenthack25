import React from 'react';

export default function TruckCard({ truck, company, assignedDriver, onBook }) {
  return (
    <div className="bg-white rounded shadow p-4 flex items-center space-x-4">
      <img
        src={truck.imageUrl}
        alt={truck.name}
        className="w-24 h-12 rounded object-cover"
        loading="lazy"
      />
      <div className="flex-1">
        <h3 className="text-lg font-semibold">{truck.name}</h3>
        <p className="text-gray-600">Company: {company?.name || "N/A"}</p>
        <p className={`font-medium ${truck.available ? 'text-green-600' : 'text-red-600'}`}>
          {truck.available ? "Available" : `Assigned to ${assignedDriver?.name || "Unknown"}`}
        </p>
      </div>
      {truck.available && (
        <button
          onClick={() => onBook(truck.id)}
          className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded transition"
        >
          Book Now
        </button>
      )}
    </div>
  );
}
