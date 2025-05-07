options(repos = c(CRAN = "https://cloud.r-project.org"))

cran_packages <- c("arules", "caret", "caTools", "e1071", "ggplot2", "h2o", "kernlab", "randomForest", "SnowballC", "tm", "xgboost")
external_packages <- list(
  ElemStatLearn = "https://cran.r-project.org/src/contrib/Archive/ElemStatLearn/ElemStatLearn_2015.6.26.2.tar.gz"
)

install_if_missing <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    install.packages(pkg)
  }
}

install_if_missing_external <- function(pkg, url) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    install.packages(url, repos = NULL, type = "source")
  }
}

lapply(cran_packages, install_if_missing)
mapply(install_if_missing_external, names(external_packages), external_packages)

if ("renv" %in% rownames(installed.packages())) {
  renv::snapshot()
}
