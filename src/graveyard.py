    # print("Statistical properties of random data")
    # print(randomdata.describe())

    # Heat map for best numbers, More work needed

    ax = plt.gca()
    ax.invert_yaxis()
    plt.gcf().set_size_inches(20, 25)
    heatmap = plt.pcolor(
        np.reshape(np.array(freqs), (5, 5)), cmap=plt.cm.Blues)
    plt.show()

    # Machine Learning part
    X = np.array(alldata)
    # We will code with "0" the human combinations, and with "1" the random
    # combinations
    y = np.array([0] * winning_numbers + [1] * randomdata_len)

    # We split our data set in 2 parts :
    # A "train set" (80% of the available data) : used to train the model
    # A "test set" (20% of the available data) : used to evaluate the model
    # performance
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=43)

    # In this example we use a Random Forest model. Many other are available
    # in the scikit-learn library
    model = RandomForestClassifier(n_estimators=100)

    # We train the model on the "train set"
    model.fit(X_train, y_train)
