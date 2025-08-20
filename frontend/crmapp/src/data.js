export const companies = [
  { id: 1, name: "American Freight Co." },
  { id: 2, name: "USA Trucking Logistics" },
];

export const trucks = [
  { id: 1, name: "Truck A", available: true, companyId: 1 },
  { id: 2, name: "Truck B", available: false, companyId: 2 },
  { id: 3, name: "Truck C", available: true, companyId: 1 },
];

export const drivers = [
  { id: 1, name: "John Doe", assignedTruckId: 2, companyId: 2 },
  { id: 2, name: "Jane Smith", assignedTruckId: null, companyId: 1 },
];

export const invoices = [
  { id: 1, driverId: 1, amount: 500, paid: true },
  { id: 2, driverId: 2, amount: 300, paid: false },
];

export function assignTruck(driverId, truckId) {
  const truck = trucks.find(t => t.id === truckId);
  const driver = drivers.find(d => d.id === driverId);
  if (truck && driver && truck.available) {
    truck.available = false;
    driver.assignedTruckId = truck.id;
  }
}

export function unassignTruck(driverId) {
  const driver = drivers.find(d => d.id === driverId);
  if (driver && driver.assignedTruckId) {
    const truck = trucks.find(t => t.id === driver.assignedTruckId);
    truck.available = true;
    driver.assignedTruckId = null;
  }
}
