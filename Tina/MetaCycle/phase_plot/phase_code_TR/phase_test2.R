# Load necessary libraries
library(circlize)

# Define the function to round to the nearest multiple of 3
round_to_three <- function(x) {
  #as.integer(round(x / 6) * 6)
  as.integer(round(x / 3) * 3)
}

# Define the phasedraw function
phasedraw <- function(phase, scalenum, colphase) {
  library(circlize)
  plot(c(-1, 1), c(-1, 1), type = "n", axes = FALSE, ann = FALSE, asp = 1)
  
  # Draw grey sectors to represent the background of the phase plot
  for(i in seq(0, 135, by = 45)){
    draw.sector(i, i+45, 1, col=NA, border="lightgrey")
  }
  
  # Define the specific degrees for the four angles you need
  degree <- cbind(c(105,75), c(15,360-15), c(285,255), c(195,165))
  
  # Only use the four angles from lagnum
  lagnum <- c("0", "3", "6", "9", "12", "15","18","21")
  
  # Draw colored sectors for actual data
  for(i in 1:8){
  #for(i in 1:4){
    lag_phase <- as.integer(phase[as.character(lagnum[i])])
    if(!is.na(lag_phase) && lag_phase > 0){
      draw.sector(degree[1,i], degree[2,i], lag_phase/scalenum, col=colphase)
    }
  }
  
  # Add scale text
  text(-0.1, 0.25, scalenum*0.25)
  text(-0.1, 0.5, scalenum*0.5)
  text(-0.1, 0.75, scalenum*0.75)
  text(-0.1, 1, scalenum*1)
}

# Function to process data and create a phase plot
process_data_and_plot <- function(file_name, colphase) {
  data <- read.table(file_name, header=TRUE, sep="\t", stringsAsFactors = FALSE)
  data$meta2d_phase <- as.numeric(as.character(data$meta2d_phase))
  data$meta2d_phase[is.na(data$meta2d_phase)] <- 0
  
  data$rounded_phase <- sapply(data$meta2d_phase, round_to_three)
  data$rounded_phase <- ifelse(data$rounded_phase == 24, 0, data$rounded_phase)
  
  phase_counts <- table(as.integer(data$rounded_phase))
  max_scale_num <- max(phase_counts)
  
  phasedraw(phase_counts, max_scale_num, colphase)
}

# Start PDF device
pdf("GF_metacycle_8.pdf", width=5, height=5)

# Process and plot the dataset
file_names <- c("meta2d_GF3.txt") # Update with your actual file path
colors <- c("hotpink1", "blue", "green", "orange") # You can choose your own colors

for(i in 1:length(file_names)) {
  process_data_and_plot(file_names[i], colors[i])
}

# End PDF device
dev.off()

