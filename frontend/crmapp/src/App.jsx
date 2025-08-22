import React, { useState } from 'react';
import Sidebar from './components/Sidebar.jsx';
import HeroSection from './components/HeroSection.jsx';
import DriverCard from './components/DriverCard.jsx';
import TruckCard from './components/Truckcard.jsx';
import CompanyCard from './components/CompanyCard.jsx';

import {
  trucks,
  drivers,
  companies,
  invoices,
  assignTruck,
  unassignTruck,
} from './data.js';

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

  // Helper to get company by id
  const getCompany = (id) => companies.find(c => c.id === id);

  // Helper to get driver assigned to truck
  const getAssignedDriver = (truckId) =>
    driversState.find(d => d.assignedTruckId === truckId);

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar trucks={trucksState} drivers={driversState} companies={companies} />
      <div className="flex-grow overflow-auto">
        <HeroSection />
        <main className="p-6 max-w-7xl mx-auto space-y-10">
          <section>
            <h2 className="text-2xl font-semibold mb-4">Drivers</h2>
            <div className="grid gap-6 md:grid-cols-2">
              {driversState.map(driver => (
                <DriverCard
                  key={driver.id}
                  driver={driver}
                  assignedTruck={trucksState.find(t => t.id === driver.assignedTruckId)}
                  company={getCompany(driver.companyId)}
                />
              ))}
            </div>
          </section>

          <section>
            <h2 className="text-2xl font-semibold mb-4">Trucks</h2>
            <div className="grid gap-6 md:grid-cols-2">
              {trucksState.map(truck => (
                <TruckCard
                  key={truck.id}
                  truck={truck}
                  company={getCompany(truck.companyId)}
                  assignedDriver={getAssignedDriver(truck.id)}
                />
              ))}
            </div>
          </section>

          <section>
            <h2 className="text-2xl font-semibold mb-4">Companies</h2>
            <div className="grid gap-6 md:grid-cols-3">
              {companies.map(company => (
                <CompanyCard key={company.id} company={company} />
              ))}
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

          <section className="bg-white rounded shadow p-6">
            <h2 className="text-2xl font-semibold mb-4">About Our Services</h2>
            <p className="mb-4">
              We provide nationwide transportation services specializing in trucking vehicles and logistics management...
            </p>
            <p className="mb-4">
              Our services cover freight transportation, logistics coordination, route planning, and driver management in the United States.
            </p>
            {/* Embed Map or Routes image */}
            <img
              src="https://i.pinimg.com/736x/96/0a/17/960a179639a5a4920de7d01ba0eb87cb.jpg"
              alt="Service Map"
              className="w-full h-64 object-cover rounded"
            />
          </section>
        </main>
      </div>
    </div>
  );
}
