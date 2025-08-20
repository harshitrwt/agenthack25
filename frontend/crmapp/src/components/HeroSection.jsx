import React from 'react';

export default function HeroSection() {
  return (
    <section
      className="relative h-[500px] w-full text-white flex flex-col justify-center items-center text-center px-6"
      style={{
        backgroundImage: "url('https://media.istockphoto.com/id/1445074332/photo/bright-colorful-big-rigs-semi-trucks-with-semi-trailers-standing-in-the-row-on-truck-stop.jpg?s=612x612&w=0&k=20&c=N5fVLeFT119Yv0QSH2Z9UgDXFOLW1qXHqL0p7EPkPRs=')",
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
      }}
    >
      {/* Dark overlay */}
      <div className="absolute inset-0 bg-black bg-opacity-60"></div>

      {/* Content */}
      <div className="relative z-10 max-w-4xl">
        <h1 className="text-5xl font-extrabold mb-4 drop-shadow-lg">
          American Freight Management
        </h1>
        <p className="text-xl max-w-xl mx-auto mb-8 drop-shadow-md">
          Reliable Truck & Vehicle Transportation Services Across the United States.
          Efficient Fleet Management, Driver Allocation, and Real-Time Logistics Solutions.
        </p>
        <button className="px-6 py-3 bg-red-600 hover:bg-red-700 rounded font-semibold shadow-lg transition duration-300">
          Get Started
        </button>
      </div>
    </section>
  );
}
