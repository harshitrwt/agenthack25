import React from 'react';

export default function Sidebar({ trucks, drivers, companies }) {
  return (
    <aside className="w-80 p-4 bg-gray-900 text-white min-h-screen flex flex-col gap-8 overflow-auto">
      <h2 className="text-xl font-bold mb-4 border-b border-gray-700 pb-2">Dashboard</h2>

      <div>
        <h3 className="text-lg font-semibold mb-3 border-b border-gray-700 pb-1">Trucks</h3>
        <ul>
          {trucks.map(truck => (
            <li
              key={truck.id}
              className={`flex items-center py-2 px-2 rounded mb-1 ${
                truck.available ? 'bg-green-500' : 'bg-yellow-500'
              }`}
            >
              <img
                src={truck.imageUrl}
                alt={truck.name}
                className="w-12 h-8 object-cover rounded mr-3 flex-shrink-0"
                loading="lazy"
              />
              <span className="truncate">{truck.name} - {truck.available ? 'Available' : 'In Use'}</span>
            </li>
          ))}
        </ul>
      </div>

      <div>
        <h3 className="text-lg font-semibold mb-3 border-b border-gray-700 pb-1">Drivers</h3>
        <ul>
          {drivers.map(driver => (
            <li key={driver.id} className="flex items-center py-2 px-2 rounded bg-gray-800 mb-1">
              <img
                src={driver.imageUrl}
                alt={driver.name}
                className="w-12 h-12 object-cover rounded-full mr-3 flex-shrink-0"
                loading="lazy"
              />
              <span className="truncate">{driver.name}</span>
            </li>
          ))}
        </ul>
      </div>

      <div>
        <h3 className="text-lg font-semibold mb-3 border-b border-gray-700 pb-1">Companies</h3>
        <ul>
          {companies.map(company => (
            <li key={company.id} className="flex flex-col bg-gray-800 rounded p-2 mb-2">
              <div className="flex items-center">
                <img
                  src={company.imageUrl}
                  alt={company.name}
                  className="w-12 h-12 object-cover rounded-full mr-3 flex-shrink-0"
                  loading="lazy"
                />
                <span className="truncate text-white text-lg font-medium">{company.name}</span>
              </div>
              <p className="text-gray-400 text-sm mt-1 ml-15">{company.title}</p>
            </li>
          ))}
        </ul>
      </div>
    </aside>
  );
}
