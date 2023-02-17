# a code of anomalies detection using PCA approach
import numpy as np
from sklearn.decomposition import PCA
def libPCA():
  # Load the data and using PCA function to extract the anomalies

  data = np.loadtxt('data.txt')
  pca = PCA(n_components=2)
  pca.fit(data)

  # Transform the data using PCA that we're gonna detail later

  transformed_data = pca.transform(data)

  # Calculate the distance from the center of the data for each point

  distances = np.linalg.norm(transformed_data, axis=1)

  # Identify the points that are potential anomalies and threats to the data system

  anomalies = np.where(distances > np.mean(distances) + 3 * np.std(distances))[0]
  print(anomalies)
def PCA():
  
  #now whihtout the library of PCA 


  # Load the data
  data = np.loadtxt('data.txt')
  #to detail the pca approach we neet 4 steps
  # first : Calculate the covariance matrix
  covariance_matrix = np.cov(data.T)

  # second : Calculate the eigenvalues and eigenvectors of the covariance matrix
  eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

  # third : Sort the eigenvalues and eigenvectors in descending order
  idx = eigenvalues.argsort()[::-1]
  eigenvalues = eigenvalues[idx]
  eigenvectors = eigenvectors[:, idx]

  # finally :Select the top n eigenvectors and project the data onto the resulting subspace
  n = 2
  projected_data = data.dot(eigenvectors[:, :n])


  # Calculate the distance from the center of the data for each point
  distances = np.linalg.norm(projected_data, axis=1)
  #whith this we re gonna get the data that are whithout a doubt coming from an unwanted source
  # by identifyinh there sources nad putting a tag on them
  # Identify the points that are more than 3 standard deviations from the mean distance
  anomalies = np.where(distances > np.mean(distances) + 3 * np.std(distances))[0]

  # Print the indices of the anomalous points
  print(anomalies)
