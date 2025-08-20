import React, { useState } from 'react';
import Sidebar from './components/sidebar.jsx';
import HeroSection from './components/HeroSection.jsx';
import {
  trucks,
  drivers,
  companies,
  invoices,
  assignTruck,
  unassignTruck,
} from './data.js';

const truckImage = "https://plus.unsplash.com/premium_photo-1664695368767-c42483a0bda1?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJ1Y2t8ZW58MHx8MHx8fDA%3D";
const driverImage = "https://images.squarespace-cdn.com/content/v1/5e73c9f4230dd951bffdcee0/e9350177-c899-4590-9b90-bf5a1d0eae53/Bright-Future-Truck-Driving-Jobs.jpg";

export default function App() {
  const [trucksState, setTrucksState] = useState(trucks);
  const [driversState, setDriversState] = useState(drivers);
  const [invoicesState] = useState(invoices);

  function handleAssign(driverId, truckId) {
    assignTruck(driverId, truckId);
    setDriversState([...drivers]);
    setTrucksState([...trucks]);
  }

  function handleUnassign(driverId) {
    unassignTruck(driverId);
    setDriversState([...drivers]);
    setTrucksState([...trucks]);
  }

  const getCompanyName = (companyId) => {
    const company = companies.find(c => c.id === companyId);
    return company ? company.name : "Unknown";
  }

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar trucks={trucksState} drivers={driversState} companies={companies} />
      <div className="flex-grow overflow-auto">
        <HeroSection />
        <main className="p-6 max-w-7xl mx-auto space-y-10">
          <section>
            <h2 className="text-2xl font-semibold mb-4">Driver and Truck Assignments</h2>
            <div className="space-y-4">
              {driversState.map(driver => {
                const assignedTruck = trucksState.find(t => t.id === driver.assignedTruckId);
                return (
                  <div key={driver.id} className="p-4 bg-white rounded shadow flex justify-between items-center">
                    <div className="flex items-center space-x-4">
                      {/* Driver Image */}
                      <img 
                        src={driverImage}
                        alt={driver.name}
                        className="w-14 h-14 rounded-full object-cover flex-shrink-0"
                        loading="lazy"
                      />
                      {/* Driver Info */}
                      <div>
                        <p className="font-medium">{driver.name}</p>
                        <p className="text-sm text-gray-500">Company: {getCompanyName(driver.companyId)}</p>
                      </div>
                    </div>

                    <div className="flex items-center space-x-4">
                      {/* Truck image and info or message */}
                      {assignedTruck ? (
                        <>
                          <img 
                            src={truckImage}
                            alt={assignedTruck.name}
                            className="w-20 h-12 object-cover rounded flex-shrink-0"
                            loading="lazy"
                          />
                          <p className="text-gray-700">{assignedTruck.name}</p>
                        </>
                      ) : (
                        <span>No truck assigned</span>
                      )}
                    </div>

                    <div>
                      {assignedTruck ? (
                        <button
                          onClick={() => handleUnassign(driver.id)}
                          className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
                        >
                          Unassign Truck
                        </button>
                      ) : (
                        <select
                          className="border rounded px-2 py-1"
                          onChange={e => handleAssign(driver.id, Number(e.target.value))}
                          defaultValue=""
                        >
                          <option value="" disabled>Assign Truck</option>
                          {trucksState.filter(t => t.available).map(truck => (
                            <option key={truck.id} value={truck.id}>
                              {truck.name} - {getCompanyName(truck.companyId)}
                            </option>
                          ))}
                        </select>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          </section>

          <section>
            <h2 className="text-2xl font-semibold mb-4">Invoices</h2>
            <table className="w-full bg-white rounded shadow">
              <thead>
                <tr className="border-b bg-gray-50">
                  <th className="text-left p-2">Driver</th>
                  <th className="text-left p-2">Amount ($)</th>
                  <th className="text-left p-2">Status</th>
                </tr>
              </thead>
              <tbody>
                {invoicesState.map(invoice => {
                  const driver = driversState.find(d => d.id === invoice.driverId);
                  return (
                    <tr key={invoice.id} className="border-b hover:bg-gray-100">
                      <td className="p-2">{driver ? driver.name : "Unknown"}</td>
                      <td className="p-2">{invoice.amount}</td>
                      <td className={`p-2 font-semibold ${invoice.paid ? 'text-green-600' : 'text-red-600'}`}>
                        {invoice.paid ? "Paid" : "Pending"}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </section>
        </main>
      </div>
    </div>
  );
}
