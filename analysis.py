import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

class Analysis:
    def __init__(self, bins=50, clip_ke=None):
        """
        bins: number of histogram bins
        clip_ke: optional float, clip all KE values above this for better visualization
        """
        self.bins = bins
        self.clip_ke = clip_ke
        self.ke_list = []

        # Create figure and axes
        self.fig, self.ax = plt.subplots()
        plt.ion()  # interactive mode
        plt.show()

    def update_ke(self, particles):
        """Calculate kinetic energy for all particles and optionally clip high values."""
        self.ke_list = [0.5 * (p.vx**2 + p.vy**2) for p in particles]

        if self.clip_ke is not None:
            # Clip extremely high KE values for better histogram visibility
            self.ke_list = [min(ke, self.clip_ke) for ke in self.ke_list]

    def plot(self):
        """Plot the KE histogram with dynamic range and particle count check."""
        if not self.ke_list:
            return

        self.ax.cla()  # clear previous plot

        # Plot histogram
        self.ax.hist(self.ke_list, bins=self.bins, color='orange', alpha=0.7, edgecolor='black')
        self.ax.set_xlabel("Kinetic Energy")
        self.ax.set_ylabel("Number of particles")
        self.ax.set_title(f"KE Distribution (N={len(self.ke_list)})")

        # Optionally show min/max KE on the plot
        min_ke = min(self.ke_list)
        max_ke = max(self.ke_list)
        self.ax.text(0.95, 0.95, f"KE min={min_ke:.1f}\nKE max={max_ke:.1f}",
                     horizontalalignment='right',
                     verticalalignment='top',
                     transform=self.ax.transAxes,
                     bbox=dict(facecolor='white', alpha=0.7))

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()  # process GUI events
        plt.pause(0.001)  # let Tkinter update