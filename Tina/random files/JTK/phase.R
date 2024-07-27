# Load necessary library
library(circlize)

# Define the phasedraw function
phasedraw <- function(phase, scalenum, colphase) {
  plot(c(-1, 1), c(-1, 1), type = "n", axes = FALSE, ann = FALSE, asp = 1)
  for(i in 1:7) {
    for(j in 1:4) {
      draw.sector((i-1)*45, i*45, j*0.25, col=NA, border="lightgrey")
    }
  }

  lagnum <- c("0", "3", "6", "9", "12", "15", "18", "21")
  degree <- cbind(c(105, 75), c(60, 30), c(15, 360-15), c(330, 300), c(285, 255), c(240, 210), c(195, 165), c(150, 120))
  for(i in 1:8) {
    if(is.na(phase[as.character(lagnum[i])])) {
      next
    } else {
      draw.sector(degree[1, i], degree[2, i], phase[as.character(lagnum[i])] / scalenum, col=colphase)
    }
  }
  text(-0.1, 0.25, scalenum*0.25)
  text(-0.1, 0.5, scalenum*0.5)
  text(-0.1, 0.75, scalenum*0.75)
  text(-0.1, 1, scalenum*1)
}

# Function to process data and create a phase plot
process_data_and_plot <- function(file_name, colphase) {
  data <- read.table(file_name, header=TRUE, sep="\t")
  phase_counts <- table(data$LAG)
  max_scale_num <- max(phase_counts)
  phasedraw(phase_counts, max_scale_num, colphase)
}

# Start PDF device
pdf("JTKPhase_Combined.pdf", width=5, height=5)

# Process and plot each dataset
file_names <- c("JTK.GF.txt", "JTK.WT_Hdac3.txt")
colors <- c("hotpink1", "blue") # You can choose your own colors

for(i in 1:length(file_names)) {
  process_data_and_plot(file_names[i], colors[i])
}

# End PDF device
dev.off()

