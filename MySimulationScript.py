from m5.objects import System, X86IntelMPIO, TimingSimpleCPU, DDR3_1600_8x8, SimpleMemory

system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

system.cpu = TimingSimpleCPU()
system.membus = SystemXBar()
system.memory = SimpleMemory(latency='10ns', bandwidth='100GB/s')
system.cpu.icache_port = system.membus.slave
system.cpu.dcache_port = system.membus.slave
