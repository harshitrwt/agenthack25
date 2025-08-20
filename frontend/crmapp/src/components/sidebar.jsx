import React from 'react';

const truckImage = "https://plus.unsplash.com/premium_photo-1664695368767-c42483a0bda1?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJ1Y2t8ZW58MHx8MHx8fDA%3D";
const driverImage = "https://images.squarespace-cdn.com/content/v1/5e73c9f4230dd951bffdcee0/e9350177-c899-4590-9b90-bf5a1d0eae53/Bright-Future-Truck-Driving-Jobs.jpg";
const companyImage = "https://res.cloudinary.com/protenders/image/upload/c_limit,d_missing,dpr_3.0,f_auto,fl_progressive:semi,q_auto:eco,w_500/9068ee4c3e40bbb22db9b4ef8ca43d0d.jpg";

export default function Sidebar({ trucks, drivers, companies }) {
  return (
    <aside className="w-80 p-4 bg-gray-900 text-white min-h-screen flex flex-col gap-8 overflow-auto">
      <h2 className="text-xl font-bold mb-4 border-b border-gray-700 pb-2">Dashboard</h2>

      <div>
        <h3 className="text-lg font-semibold mb-3 border-b border-gray-700 pb-1">Trucks</h3>
        <ul>
          {trucks.map(truck => (
            <li key={truck.id} className={`flex items-center py-2 px-2 rounded mb-1 ${truck.available ? 'bg-green-700' : 'bg-red-700'}`}>
              <img 
                src={truckImage} 
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
                src={driverImage}
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
            <li key={company.id} className="flex items-center py-2 px-2 rounded bg-gray-800 mb-1">
              <img 
                src={companyImage}
                alt={company.name}
                className="w-12 h-12 object-cover rounded-full mr-3 flex-shrink-0"
                loading="lazy"
              />
              <span className="truncate">{company.name}</span>
            </li>
          ))}
        </ul>
      </div>
    </aside>
  );
}
