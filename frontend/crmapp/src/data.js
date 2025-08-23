export const companies = [
  { id: 1, name: "American Freight Co.", title: "Tied with American Freight Co.", imageUrl: "https://i.pinimg.com/1200x/8f/f7/83/8ff78354692268f708a339f187bc90cc.jpg" },
  { id: 2, name: "USA Trucking Logistics", title: "Tied with USA Trucking Logistics", imageUrl: "https://i.pinimg.com/1200x/5b/50/e5/5b50e562f28fc54cc88c939e59597b73.jpg" },
  { id: 3, name: "VolksWagen Gnc.", title: "Tied with National Haulers Inc.", imageUrl: "https://i.pinimg.com/736x/53/3f/dc/533fdcce92ee6404cfd5a4262e87fd95.jpg" },
  { id: 4, name: "Nestle Co.", title: "Tied with Nestle Co.", imageUrl: "https://i.pinimg.com/1200x/82/9b/90/829b90e9eb6f43993dd9c2c7c96954de.jpg" },
  { id: 5, name: "Nivea Movers LLC", title: "Tied with Cargo Movers LLC", imageUrl: "https://i.pinimg.com/736x/41/04/5c/41045c8149f61d9bb7a02e6a36d6e328.jpg" },
  { id: 6, name: "Interstate Trucking", title: "Tied with Interstate Trucking", imageUrl: "https://i.pinimg.com/736x/91/17/45/911745584b4787eb06240f7ab06e731a.jpg" },
  { id: 7, name: "LogiTrans Corp.", title: "Partnered with LogiTrans Corp.", imageUrl: "https://i.pinimg.com/1200x/8f/83/d4/8f83d4e6a12e1a3385dc7503c40d4876.jpg" },
];

export const trucks = [
  { id: 1, name: "Big Rig", available: true, companyId: 1, imageUrl: "https://plus.unsplash.com/premium_photo-1664695368767-c42483a0bda1?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0" },
  { id: 2, name: "Iron Stallion", available: false, companyId: 2, imageUrl: "https://t4.ftcdn.net/jpg/02/51/99/07/360_F_251990717_OdI3jNyvxecAhbS3wJaoa3B6JJOf3S2I.jpg" },
  { id: 3, name: "Steel Mustang", available: true, companyId: 3, imageUrl: "https://preview.redd.it/rc53gw230zl81.jpg?width=640&crop=smart&auto=webp&s=e3b2b45c863ca462cda69599ed65ad6ff9decce6" },
  { id: 4, name: "Liberty", available: true, companyId: 4, imageUrl: "https://preview.redd.it/heres-more-american-semi-trucks-in-europe-there-are-a-few-v0-bn6s9dckq5m81.jpg?width=640&crop=smart&auto=webp&s=6eeb8b262302a381e5e2c10152795f39bdfb52e5" },
  { id: 5, name: "Hauler", available: false, companyId: 5, imageUrl: "https://plus.unsplash.com/premium_photo-1733342421852-3bce709563e4?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8YW1lcmljYW4lMjB0cnVja3xlbnwwfHwwfHx8MA%3D%3D" },
];

export const drivers = [
  { id: 1, name: "Sam", assignedTruckId: 2, companyId: 2, imageUrl: "https://images.squarespace-cdn.com/content/v1/5e73c9f4230dd951bffdcee0/e9350177-c899-4590-9b90-bf5a1d0eae53/Bright-Future-Truck-Driving-Jobs.jpg" },
  { id: 2, name: "Jane Smith", assignedTruckId: null, companyId: 1, imageUrl: "https://cdn.prod.website-files.com/5f70f0246e0318453837c2b9/645e55802a8121645040fbed_hiring%20a%20truck%20driver.webp" },
  { id: 3, name: "Tom Brown", assignedTruckId: 3, companyId: 3, imageUrl: "https://www.ohiotrucks.com/wp-content/uploads/10-tips-for-becoming-semi-truck-owner-operator.jpg" },
  { id: 4, name: "Emily Davis", assignedTruckId: null, companyId: 4, imageUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrnrjJEPDI4xn30MqSmwSjFmy99iqZZZq53A&s" },
  { id: 5, name: "Michael Wilson", assignedTruckId: 5, companyId: 5, imageUrl: "https://cdn.prod.website-files.com/5f70f0246e0318453837c2b9/645e490635327ca9b661bb47_becoming%20a%20truck%20driver.webp" },
];

export const invoices = [
  { id: 1, driverId: 1, amount: 1500, paid: true },
  { id: 2, driverId: 2, amount: 1300, paid: false },
  { id: 3, driverId: 3, amount: 2450, paid: true },
  { id: 4, driverId: 4, amount: 1600, paid: false },
  { id: 5, driverId: 5, amount: 3750, paid: true },
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
