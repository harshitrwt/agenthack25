import React from 'react';

export default function HeroSection() {
  return (
    <section
      className="relative h-[500px] w-full text-white flex flex-col justify-center items-center text-center px-6"
      style={{
        backgroundImage: "url('https://i.pinimg.com/1200x/94/79/1a/94791a03f73dce4ff6afbcabadb006e7.jpg')",
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
      }}
    >
      
      <div className="absolute inset-0 bg-black bg-opacity-20"></div>

      
      <div className="relative z-10 max-w-4xl">
        <h1 className="text-5xl font-extrabold mb-4 drop-shadow-lg">
          EuroBridge Trucking
        </h1>
        <p className="text-xl max-w-xl mx-auto mb-8 drop-shadow-md">
          Reliable Truck & Vehicle Transportation Services Across the Europe. Efficient Fleet Management, Driver Allocation, and Real-Time Logistics Solutions.
        </p>
        <button className="px-6 py-3 bg-yellow-500 hover:bg-yellow-700 rounded font-semibold shadow-lg transition duration-300">
          Get Started
        </button>
      </div>
    </section>
  );
}
